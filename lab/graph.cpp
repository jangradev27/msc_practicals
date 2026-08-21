#include<iostream>
#include<vector>
#include<unordered_map>
#include<unordered_set>
#include<climits>
#include<cstdlib>
#include<random>
#include<fstream>
#include<ctime>

using namespace std;

class Graph{

    int n;
    unordered_map<int,unordered_set<int>> adjlist;

    public:
        Graph(int n,int i){
            this->n=n;
            this->fileCounter=i;
        }

        void insertEdge(int u,int v){
            if(u>this->n || u<1 || v>this->n || v<1){
                cout<<"edges must be between 1 and "<<n<<endl;
                return;
            }

            adjlist[u].insert(v);
            adjlist[v].insert(u);

        }

        void showAdjList(){

             for(auto it=adjlist.begin();it!=adjlist.end();it++){
                 cout<<it->first<<"-> ";

                 for(auto &i:it->second){
                     cout<<i<<" ";
                 }

                 cout<<endl;
             }
        }

       
        void dfs(int src, vector<bool> &visited){

            visited[src]=true;

            for(auto &j:adjlist[src]){

                if(!visited[j]){
                    dfs(j,visited);
                }
            }
        }

        bool isConnected(){

            vector<bool> visited(n+1,false);

            int count=0;

            for(int i=1;i<=n;i++){

                if(!visited[i]){

                    count++;

                    dfs(i,visited);
                }
            }

            if(count>1){
                cout<<"Graph is not connected";
            }
            else{
                cout<<"Graph is connected";
            }
            return count==1;
        }


};


int main(){

    

    return 0;
}