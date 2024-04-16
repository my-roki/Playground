public class Permutations {
    public static void main(String[] args) {
        int n = 3;
        int[] arr = { 1, 2, 3 };
        int[] output = new int[n];
        boolean[] visited = new boolean[n];

        System.out.println("Permutations with swap are:");
        permutation_with_swap(arr, 0, n, 2);

        System.out.println("Permutations with DFS are:");
        permutation_with_DFS(arr, output, visited, 0, n, 2);
    }

    /**
     * Generate all permutations of size r from an array of size n using swapping
     * @param arr : input array
     * @param depth : current depth
     * @param n : size of input array
     * @param r : size of permutation
     */
    static void permutation_with_swap(int[] arr, int depth, int n, int r) {
        if (depth == r) {
            print(arr, r);
            return;
        }

        for (int i = depth; i < n; i++) {
            swap(arr, depth, i);
            permutation_with_swap(arr, depth + 1, n, r);
            swap(arr, depth, i);
        }
    }

    static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    /**
     * Generate all permutations of size r from an array of size n using DFS
     * @param arr : input array
     * @param output : output array
     * @param visited : boolean array to keep track of visited elements
     * @param depth : current depth
     * @param n : size of input array
     * @param r : size of permutation
     */
    static void permutation_with_DFS(int[] arr, int[] output, boolean[] visited, int depth, int n, int r) {
        if (depth == r) {
            print(output, r);
            return;
        }

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                visited[i] = true;
                output[depth] = arr[i];
                permutation_with_DFS(arr, output, visited, depth + 1, n, r);
                visited[i] = false;
            }
        }

    }

    // 배열 출력
    static void print(int[] arr, int r) {
        for (int i = 0; i < r; i++)
            System.out.print(arr[i] + " ");
        System.out.println();
    }
}
