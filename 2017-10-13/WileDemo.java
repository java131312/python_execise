/*
	while循环的格式

	基本格式：
		while(判断条件语句){
			循环体语句;
		}
	完整的格式：
		初始化表达式语句
		while(判断条件语句){
			循环体语句;
			控制条件语句;
		}
	执行流程
		a.执行初始化表达式语句
		b.执行判断条件语句，看其结果是true还是false
			如果是false,则结束循环
			如果是true,则继续执行
		c.继续执行循环体语句
		d.执行控制条件语句
		e.回到b
	初始化表达式语句只执行一次。
*/
class WhileDemo
{
	public static void main(String[] args){
		//需求： 在控制台输出10次"helloworld"
		/*
			初始化表达式语句
			while(判断条件语句){
				循环体语句;
				控制条件语句;
			}
		*/
		int i = 0;
		while(i < 10) {
			System.out.println("helloworld");
			i++;
		}

		System.out.println("---------------------");

		//需求：请在控制台输出数据1-10
		int x = 1;
		while( x <= 10){
			System.out.println(x);
			x++;
		}
	}
}