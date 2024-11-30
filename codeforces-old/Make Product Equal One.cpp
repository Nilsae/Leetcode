  #include<bits/stdc++.h>
  using namespace std;
  int main(){
  long long n,ans=0;
  cin>>n;
  long long a[n];
  long long odd=0;bool b=false;
  for(int i=0;i<n;i++) cin>>a[i];
  for(int i=0;i<n;i++){
    if(a[i]<0){
      ans+=(-1)*a[i];
      ans-=1;
      odd++;
    }
    else if(a[i]>0){
      ans+=a[i];
      ans-=1;
    }
    else{
      ans+=1;
      b=true;
    }
  }
  if(!b){
  if (odd %2==1){
    ans+=2;

  }
}
  cout<<ans;





  }
