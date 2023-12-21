import os
import subprocess
import glob
import concurrent.futures


def create_folder(folder_path):
    os.makedirs(folder_path, exist_ok=True)


def run_demkf(python_executable, demkf_tool, mkf_file, output_dir):
    subprocess.run(
        [python_executable, demkf_tool, "-p", "yj1", mkf_file], cwd=output_dir
    )


def run_deyj1(python_executable, deyj1_tool, yj1_file, output_dir):
    subprocess.run([python_executable, deyj1_tool, yj1_file, "-o", output_dir])


def run_desmkf(python_executable, desmkf_tool, smkf_file, output_dir):
    subprocess.run(
        [python_executable, desmkf_tool, "-p", "rle", smkf_file], cwd=output_dir
    )


def run_derle(python_executable, derle_tool, rle_file, pat_file, output_dir):
    output_file = os.path.relpath(rle_file, start=output_dir).replace(".rle", ".bmp")
    bmp_output_path = os.path.join(output_dir, output_file)

    os.makedirs(os.path.dirname(bmp_output_path), exist_ok=True)

    subprocess.run(
        [python_executable, derle_tool, rle_file, "-o", output_dir, "-p", pat_file]
    )


def process_file_step_1(file):
    run_demkf(python_executable, demkf_tool, file, output_dir_MKF_File)


def process_file_step_2(file):
    run_deyj1(python_executable, deyj1_tool, file, output_dir_step_2)


def process_file_step_3(file):
    run_desmkf(python_executable, desmkf_tool, file, output_dir_step_3)


def process_file_step_4(file):
    run_derle(
        python_executable, derle_tool, file, PAT_dir + "/PAT.MKF", output_dir_step_4
    )


# 配置是否执行每个步骤
execute_step_1 = True
execute_step_2 = True
execute_step_3 = True
execute_step_4 = True

# 控制是否只处理第一个文件
single_file_debug_mode = False

# 每步骤的输出目录
step_1_folder = "yj1"
step_2_folder = "smkf"
step_3_folder = "rle"
step_4_folder = "bmp"

# 配置 Python 可执行文件路径
python_executable = "python"  # 或 "python3"

# 配置工具路径
tool_path = "D:/Users/couger/Downloads/Entertainment/project/sdlpal_HD/palxex/palresearch/PackageUtils/"
demkf_tool = tool_path + "demkf.py"
deyj1_tool = tool_path + "deyj1.py"
desmkf_tool = tool_path + "desmkf.py"
derle_tool = tool_path + "derle.py"

# 指定 MKF 文件的目录
mkf_dir = "D:/Users/couger/Downloads/Entertainment/project/sdlpal_HD/归档_research"

# 指定输出目录
output_base_dir = "D:/Users/couger/Downloads/Entertainment/project/sdlpal_HD/MKF"

# 指定PAT文件的目录
PAT_dir = output_base_dir

# 获取所有 MKF 文件
mkf_files = glob.glob(os.path.join(mkf_dir, "*.mkf"))
print(f"发现 {len(mkf_files)} 个 MKF 文件。")

# 统计解包数量、成功数量、失败数量
total_files = len(mkf_files)
processed_files = 0
successful_files = 0
failed_files = 0

# 是否只取第一个文件进行处理
if single_file_debug_mode:
    mkf_files = mkf_files[:1]

for mkf_file in mkf_files:
    if mkf_file:
        file_name = os.path.basename(mkf_file)
        name_without_ext = os.path.splitext(file_name)[0]
        output_dir_MKF_File = os.path.join(output_base_dir, name_without_ext)

        # 创建每个MKF文件的输出目录
        create_folder(output_dir_MKF_File)

        # 创建步骤2、3、4的输出目录
        output_dir_step_2 = os.path.join(output_dir_MKF_File, step_2_folder)
        output_dir_step_3 = os.path.join(output_dir_MKF_File, step_3_folder)
        output_dir_step_4 = os.path.join(output_dir_MKF_File, step_4_folder)

        create_folder(output_dir_step_2)
        create_folder(output_dir_step_3)
        create_folder(output_dir_step_4)

        # 配置线程池大小
        max_workers = 4  # 可根据实际情况调整

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # 第一步并发处理
            if execute_step_1:
                executor.map(process_file_step_1, mkf_files)

            # 第二步并发处理
            if execute_step_2:
                yj1_files = glob.glob(
                    os.path.join(output_dir_MKF_File, step_1_folder, "*.yj1")
                )
                executor.map(process_file_step_2, yj1_files)

            # 第三步并发处理
            if execute_step_3:
                smkf_files = glob.glob(os.path.join(output_dir_step_2, "*.smkf"))
                executor.map(process_file_step_3, smkf_files)

            # 第四步并发处理
            if execute_step_4:
                # os.chdir(output_dir_step_3)  # 修改工作目录为第三步的输出目录
                rle_files = glob.glob(os.path.join(output_dir_step_3, "*.rle"))
                executor.map(process_file_step_4, rle_files)

# 打印最终统计信息
print("\n解包过程完成。")  # 添加换行符，以便在最后显示总体解包情况
