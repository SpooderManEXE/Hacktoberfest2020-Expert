package assignmentRec2;

public class removeX {

	public static String removeX(String str){
		// int n=0;
//		 if(input.length()==0)
//		 {
//			 return "";
//		 }
//		 if(input.charAt(0)=='x')
//		 {
//		
//			 return input.substring(1);
//		 }
//		 
//		 String ans=input.charAt(0)+ removeX(input.substring(1),c);
//		return ans;
		 
{ 

// Base Case 
if (str.length() == 0) 
{ 
return ""; 
} 

if (str.charAt(0) == 'x') 
{ 

return removeX(str.substring(1)); 
} 

return str.charAt(0)+ removeX( str.substring(1)); 
} 
		 }
	
	public static void main(String[] args) {
		String s="xxbxxaxc";
		//char c='x';
		String ans=removeX(s);
		System.out.println(ans);
		
	}
}