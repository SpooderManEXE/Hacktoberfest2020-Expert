class Shape
{
	public static void main(String[] args) {
		// set output size
		final int N = 10;

		for (int i = 0; i < N; i++) {
			for (int j = 0; j <= 4 * N; j++) {
				double d1 = Math.sqrt(Math.pow(i - N, 2)
									+ Math.pow(j - N, 2));

				double d2 = Math.sqrt(Math.pow(i - N, 2)
									+ Math.pow(j - 3 * N, 2));

				if (d1 < N + 0.5 || d2 < N + 0.5) {
					System.out.print('*');
				} else {
					System.out.print(' ');
				}
			}
			System.out.print(System.lineSeparator());
		}

		for (int i = 1; i < 2 * N; i++) {
			for (int j = 0; j < i; j++) {
				System.out.print(' ');
			}

			for (int j = 0; j < 4 * N + 1 - 2 * i; j++) {
				System.out.print('*');
			}

			System.out.print(System.lineSeparator());
		}
	}
}
