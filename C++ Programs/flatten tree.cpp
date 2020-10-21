  
    int timer = 0;
	void dfs(int v, int par){
	   entr[v] = timer++;
	  for(auto u: adj[v])
	  { if (u == par) continue;
		 dfs(u, v);
	  }
	   ext[v] = timer++;
    }
		
	vector<LL> flattenedTree(2*n);
       for(int u = 0; u < n; u++)
        {
           flattenedTree[entr[u]] = s[u];
           flattenedTree[ext[u]] = -s[u]; 
        }