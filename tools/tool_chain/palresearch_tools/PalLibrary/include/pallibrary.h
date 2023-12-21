//$ Id: PalLibrary.h 1.02 2006-05-23 14:34:50 +8:00 $

/*
 * PAL Library common include file
 * 
 * Author: Lou Yihua <louyihua@21cn.com>
 *
 * Copyright 2006 Lou Yihua
 *
 * This file is part of PAL library.
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 2.1 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 * 
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA

 *
 *���ɽ����������⹫��ͷ�ļ�
 *
 * ���ߣ� Lou Yihua <louyihua@21cn.com>
 *
 * ��Ȩ���� 2006 Lou Yihua
 *
 * ���ļ��ǡ��ɽ������������һ���֡�
 *
 * �������������������������������������������GNU��ͨ�ù������֤��
 * �����޸ĺ����·�����һ���򡣻��������֤2.1�棬���ߣ��������ѡ������
 * �ν��µİ汾��������һ���Ŀ����ϣ�������ã���û���κε���������û���ʺ�
 * �ض�Ŀ�������ĵ���������ϸ����������GNU��ͨ�ù������֤��
 * 
 * ��Ӧ���Ѿ��Ϳ�һ���յ�һ��GNU��ͨ�ù������֤�Ŀ����������û�У�д�Ÿ�
 * �����������᣺51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA
*/
#pragma once

namespace PalLibrary
{
	typedef struct _DataBuffer
	{
		void			*data;
		unsigned int	length;
	} DataBuffer;

	DataBuffer DecodeYJ_1(const void *Source);
	DataBuffer EncodeYJ_1(const void *Source, unsigned int SourceLength);
	DataBuffer DecodeWin(const void *Source);
	DataBuffer EncodeWin(const void *Source, unsigned int SourceLength);
	DataBuffer DecodeRNG(const void *Source, void *PrevFrame);
	DataBuffer EncodeRNG(const void *PrevFrame, const void *CurFrame);
}
