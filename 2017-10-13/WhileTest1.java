class WhileTest1
{
	public static void main(String[] args){
		// ͳ��"ˮ�ɻ���"���ж��ٸ�  100-999
		//forѭ�����
		//����һ��ͳ�Ʊ�����������¼ˮ�ɻ��ĸ���
		int count = 0;

		for( int i = 100; i <= 999; i++){
			//ÿһ�α�����������i
			//������Ҫ���ж����i�Ƿ���ˮ�ɻ���

			//��ȡ������ĸ���Ϊ�ϵ�����
			int ge = i%10;
			int shi = i / 10 % 10;
			int bai = i / 10 / 10 % 10;

			//��λ�ϵ����ֵ�������
			int flowerNum = ge*ge*ge + shi*shi*shi + bai*bai*bai;
			//�ж������� �Լ������Ƿ���ȣ������ȣ���ô����ˮ�ɻ���
			if(i == flowerNum){
				count++;
			}
		}

		//�������
		System.out.println(count);

		System.out.println("-----------------");

		int y = 100;
		//����һ��ͳ�Ʊ���
		int count1 = 0;

		while( y <= 999 ){
			//��ȡ������ĸ���Ϊ�ϵ�����
			int ge = y % 10;
			int shi = y / 10 % 10;
			int bai = y / 10 / 10 % 10;

			//��λ�ϵ����ֵ�������

			int flowerNum = ge*ge*ge + shi*shi*shi + bai*bai*bai;

			//�ж������� �Լ������Ƿ���ȣ� �����ȣ���ô����ˮ�ɻ���

			if( y == flowerNum ){
				count++;
			}
			y++;
		}
		//�������
		System.out.println(count);
	}
}