/*
	控制跳转语句：
		1，break;  中断
		2，continue; 继续
		3，return;  返回

	break的使用场景:
		1,switch语句中  表示结束switch语句。
		2，在循环语句中
	注意事项：离开了使用场景就没有任何意义了。

	break在循环中的作用：
		1，退出单层循环  结束单层循环
		2，退出多次循环
*/
class BreakDem
{
	public static void main(String[] args){
		//错误： 在switch或loop外部中断
		//break;
		//退出单层循环
		/*
		for(int i = 1; i <= 10; i++){
			//为了验证执行了多少次
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