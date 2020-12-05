#include <bits/stdc++.h>

#define INF 0x3f3f3f3f
#define mp make_pair
#define pb push_back
#define fori(i, n) for(int i = 0; i < n; i++)
#define For(i, a, b) for(i = a; i < b; i++)
#define roF(i, a, b) for(i = a; i > b; i--)
#define trace(x) cerr << #x << ": " << x << endl
#define _ ios_base::sync_with_stdio(0);cin.tie(0);
#define endl "\n"

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef vector<pair<int,int> > vii;

int main(){

	int v, a, e1, e2;
	set<pair<int,int>> arestas;

	cin >> v >> a;

	srand (time(NULL));

	trace(v); trace(a);
	fori(i, a){
		e1 = rand()%v + 1;
		e2 = rand()%v + 1;
		//trace(e1); trace(e2);
		if(e1 == e2 || arestas.find({min(e1, e2), max(e1, e2)}) != arestas.end()){
			i--;
			continue;
		}
		arestas.insert({min(e1, e2), max(e1, e2)});
		cout << e1 << "," << e2 << endl;
	}
	
	return 0;
}