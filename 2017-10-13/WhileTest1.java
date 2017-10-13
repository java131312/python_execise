class WhileTest1
{
	public static void main(String[] args){
		// 统计"水仙花数"共有多少个  100-999
		//for循环完成
		//定义一个统计变量，用来记录水仙花的个数
		int count = 0;

		for( int i = 100; i <= 999; i++){
			//每一次遍历的数就是i
			//我们需要来判断这个i是否是水仙花数

			//获取这个数的各个为上的数字
			int ge = i%10;
			int shi = i / 10 % 10;
			int bai = i / 10 / 10 % 10;

			//各位上的数字的立方和
			int flowerNum = ge*ge*ge + shi*shi*shi + bai*bai*bai;
			//判断立方和 以及本身是否相等，如果相等，那么就是水仙花数
			if(i == flowerNum){
				count++;
			}
		}

		//输出个数
		System.out.println(count);

		System.out.println("-----------------");

		int y = 100;
		//定义一个统计变量
		int count1 = 0;

		while( y <= 999 ){
			//获取这个数的各个为上的数字
			int ge = y % 10;
			int shi = y / 10 % 10;
			int bai = y / 10 / 10 % 10;

			//各位上的数字的立方和

			int flowerNum = ge*ge*ge + shi*shi*shi + bai*bai*bai;

			//判断立方和 以及本身是否相等， 如果相等，那么就是水仙花数

			if( y == flowerNum ){
				count++;
			}
			y++;
		}
		//输出个数
		System.out.println(count);
	}
}