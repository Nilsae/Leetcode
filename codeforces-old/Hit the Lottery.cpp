#include<bits/stdc++.h>
using namespace std;
int main(){
  long input;
  long ans=0, n=100;
  cin>>input;
  if (input>=n){
    ans+= input/n;
    input%=n;
  }
  n=20;
  if (input>=n){
    ans+= input/n;
    input%=n;
  }
  n=10;
  if (input>=n){
    ans+= input/n;
    input%=n;
  }
  n=5;
  if (input>=n){
    ans+= input/n;
    input%=n;
  }
  ans+=input;
  cout<<ans;


}
