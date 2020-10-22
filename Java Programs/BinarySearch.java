class BinarySearch  {

    public int lowerBound(int[] arr,int length,int value){
        int low=0;
        int high=length;
        while (low<high){
            int mid=(low+high)/2;
            if(value<=arr[mid])
                high=mid;
            else
                low=mid+1;
        }
        return low;
    }

    public int upperBound(int[] arr,int length,int value){
        int low=0;
        int high=length+1;
        while (low<high){
            int mid=(low+high)/2;
            if(value>=arr[mid])
                low=mid+1;
            else
                high=mid;
        }
        return low;
    }

    public int binarySearch(int[] arr,int length,int value){
        int low=0;
        int high=length;
        while (low<=high){
            int mid=(low+high)/2;
            if(value==arr[mid])
                return mid;
            else if(value>arr[mid])
                high=mid-1;
            else
                low=mid+1;
        }
        return low;
    }

    public int lowerBound(long[] arr,int length,long value){
        int low=0;
        int high=length;
        while (low<high){
            int mid=(low+high)/2;
            if(value<=arr[mid])
                high=mid;
            else
                low=mid+1;
        }
        return low;
    }

    public int upperBound(long[] arr,int length,long value){
        int low=0;
        int high=length+1;
        while (low<high){
            int mid=(low+high)/2;
            if(value>=arr[mid])
                low=mid+1;
            else
                high=mid;
        }
        return low;
    }

    public int binarySearch(long[] arr,int length,long value){
        int low=0;
        int high=length;
        while (low<=high){
            int mid=(low+high)/2;
            if(value==arr[mid])
                return mid;
            else if(value>arr[mid])
                high=mid-1;
            else
                low=mid+1;
        }
        return low;
    }

}
