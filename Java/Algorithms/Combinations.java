public class Combinations {
    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 4 };
        int n = arr.length;
        int r = 3;
        boolean[] visited = new boolean[n];
        System.out.println("Combinations with backtracking of size " + r + " are:");
        combinations_with_backtracking(arr, visited, 0, n, r);

        System.out.println("Combinations with recursion of size " + r + " are:");
        combinations_with_recursion(arr, visited, 0, n, r);

    }

    /**
     * Generate all combinations of size r from an array of size n using
     * backtracking
     * 
     * @param arr     : input array
     * @param visited : boolean array to keep track of visited elements
     * @param start   : starting index
     * @param n       : size of input array
     * @param r       : size of combination
     */
    static void combinations_with_backtracking(int[] arr, boolean[] visited, int start, int n, int r) {
        if (r == 0) {
            print(arr, visited, n);
            return;
        }

        for (int i = start; i < n; i++) {
            visited[i] = true;
            combinations_with_backtracking(arr, visited, i + 1, n, r - 1);
            visited[i] = false;
        }
    }

    /**
     * Generate all combinations of size r from an array of size n using recursion
     * 
     * @param arr     : input array
     * @param visited : boolean array to keep track of visited elements
     * @param depth   : current depth
     * @param n       : size of input array
     * @param r       : size of combination
     */
    static void combinations_with_recursion(int[] arr, boolean[] visited, int depth, int n, int r) {
        if (r == 0) {
            print(arr, visited, n);
            return;
        }

        if (depth == n) {
            return;
        }

        visited[depth] = true;
        combinations_with_recursion(arr, visited, depth + 1, n, r - 1);

        visited[depth] = false;
        combinations_with_recursion(arr, visited, depth + 1, n, r);

    }

    // 배열 출력
    static void print(int[] arr, boolean[] visited, int n) {
        for (int i = 0; i < n; i++) {
            if (visited[i]) {
                System.out.print(arr[i] + " ");
            }
        }
        System.out.println();
    }
}