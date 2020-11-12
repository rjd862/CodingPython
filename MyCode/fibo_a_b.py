
//fibonacci where 1st and 2nd number is a , b

#include <iostream>

using namespace std;
int a,b;
int fibo(int x)
{
	if(x==1)return a;
	else if(x==2)return b;
	else return fibo(x-1)+fibo(x-2);
}
int main() {
	int n;
	cin >> a>>b>>n;	
	cout<<fibo(n);
}
