/*
	������ת��䣺
		1��break;  �ж�
		2��continue; ����
		3��return;  ����

	break��ʹ�ó���:
		1,switch�����  ��ʾ����switch��䡣
		2����ѭ�������
	ע������뿪��ʹ�ó�����û���κ������ˡ�

	break��ѭ���е����ã�
		1���˳�����ѭ��  ��������ѭ��
		2���˳����ѭ��
*/
class BreakDem
{
	public static void main(String[] args){
		//���� ��switch��loop�ⲿ�ж�
		//break;
		//�˳�����ѭ��
		/*
		for(int i = 1; i <= 10; i++){
			//Ϊ����ִ֤���˶��ٴ�
			System.out.println(i);
			if( i == 3){
				break;
			}
		}*/
		wc:for(int x = 1; x <= 4; x++){
			nc:for(int y = 1; y <= 5; y++){
				if(y == 3){
					break wc;
				}
				System.out.print("*");
			}
			System.out.print("*");
		}

	}
}