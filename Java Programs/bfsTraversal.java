import java.util.Iterator;
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.Queue;

public class bfsTraversal {
    //No of vertices
    int vertex;
    LinkedList<Integer> adjacency_list[]; // Array of List holds the neighbours

    bfsTraversal(int nodes)
    {
        vertex = nodes;
        adjacency_list = new LinkedList[vertex];
        //creating objects for each entry of vertex
        for(int i = 0 ;i < vertex; i++)
        {
            adjacency_list[i] = new LinkedList<Integer>();
        }
    }
    public void cycleDetection()
    {
        boolean[] visited = new boolean[vertex];
        boolean[] recstack = new boolean[vertex];
        for(int i = 0 ; i < vertex ; i++)
        {
            if(cycleInspectorUtil(visited,recstack, i))
            {
                System.out.print("Cycle detected by starting point"+ i);
                break;
            }
        }
    }
    public boolean cycleInspectorUtil(boolean[] visited,boolean[] recstack,int i)
    {
        int curr = i;

        if(visited[curr])
            return true;
        if(recstack[curr])
            return true;

        visited[curr] = true;
        recstack[curr] = true;

        Iterator<Integer> listitr = adjacency_list[curr].listIterator();
        while(listitr.hasNext())
            cycleInspectorUtil(visited, recstack, listitr.next());
        return false;

    }
    //complete addedge Function
    public void addEdge(int src,int des)
    {
        adjacency_list[src].add(des);
        adjacency_list[des].add(src);
    }


    //complete bfs function
    void bfs(int first)
    {
        //boolean array to track them visited or unvisited
        boolean visited[] = new boolean[vertex];

        LinkedList<Integer> queue = new LinkedList<>();
        queue.add(first);
        visited[first] = true;

        while(!queue.isEmpty())
        {
            first = queue.pollFirst();
            System.out.println(first);

            //we have to traverse the current node neighbours
            // so traversal can be validated only by adjacency list right?
            Iterator<Integer> currnode = adjacency_list[first].listIterator();
            while(currnode.hasNext())
            {
                int neighbour = currnode.next();
                if(!visited[neighbour])
                {
                    visited[neighbour] = true;
                    queue.add(neighbour);
                }
            }
        }
        for(int i = 0 ; i < 7 ; i++)
            System.out.print(visited[i]+" ");
    }
    public static void main(String[] args) {
        bfsTraversal obj = new bfsTraversal(7);
        obj.addEdge(1,2);
        obj.addEdge(2,5);
        obj.addEdge(1,3);
        obj.addEdge(3,5);
        obj.addEdge(2,4);
        obj.addEdge(4,5);
        obj.addEdge(5,6);
        obj.addEdge(4,6);

        obj.bfs(2);

        //lets check cyclic detection
        // visited -- boolean array of the vertex
        // recstack -- boolean array
        obj.cycleDetection();

    }
}

