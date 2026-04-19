#include <iostream>
using namespace std;

int main(){
    int t;
    cin >> t;
    for (int i = 0; i<t; i++){
        int n,k;
        cin >> n >> k;
        int ar[n];
        for (int i = 0; i<n ; i++){
            cin >> ar[i];
        }

        int dist[n] = {0};
        int dist_no = 0;
        for (int i : ar){
            dist[i-1] = 1;
        }
        for (int i : dist){
            dist_no = dist_no + i;
        }
        // cout << "dist no is:" << dist_no << endl;
        if (dist_no >k){
            cout << -1 << endl;
            continue;;
        }
        int distinct[dist_no];
        int tem = 0;
        for (int i = 0; i<n;i++){
            if (dist[i] == 1){
                distinct[tem] = i+1;
                tem ++;
            }
        }
        cout << k*n << endl;
        for (int i = 0; i<n; i++){
            for (int j : distinct){
                cout << j << " ";
            }
            for (int j = 0; j< k - dist_no; j++){
                cout<< 1 << " " ;
            }
        }
        cout << endl;
    }


}