/*
	whileѭ���ĸ�ʽ

	������ʽ��
		while(�ж��������){
			ѭ�������;
		}
	�����ĸ�ʽ��
		��ʼ�����ʽ���
		while(�ж��������){
			ѭ�������;
			�����������;
		}
	ִ������
		a.ִ�г�ʼ�����ʽ���
		b.ִ���ж�������䣬��������true����false
			�����false,�����ѭ��
			�����true,�����ִ��
		c.����ִ��ѭ�������
		d.ִ�п����������
		e.�ص�b
	��ʼ�����ʽ���ִֻ��һ�Ρ�
*/
class WhileDemo
{
	public static void main(String[] args){
		//���� �ڿ���̨���10��"helloworld"
		/*
			��ʼ�����ʽ���
			while(�ж��������){
				ѭ�������;
				�����������;
			}
		*/
		int i = 0;
		while(i < 10) {
			System.out.println("helloworld");
			i++;
		}

		System.out.println("---------------------");

		//�������ڿ���̨�������1-10
		int x = 1;
		while( x <= 10){
			System.out.println(x);
			x++;
		}
	}
}