# Using ELimination Method One Of The Methods Equation
def computing_resource_allocation(cpu_x, cpu_y, gpu_x, gpu_y):
          # Mencari Nilai X 
          print(f"{"=" * 10} {"mencari nilai variabel x pada kedua persamaan".upper()} {"=" * 10}")
          
          # Persamaan 1(CPU): cpu = 2 * cpu_x + 4 * cpu_y
          cpu = (2 * cpu_x * 1) + (4 * cpu_y * 1)
          constant_cpu_val = 100 * 1
          # Persamaan 2(GPU): gpu = 3 * gpu_x + gpu_y
          gpu = (3 * gpu_x * 4) + (gpu_y * 4)
          constant_gpu_val = 60 * 4
          
          # Hasil Perkalian Persamaan 1(CPU) -> cpu = 2 * cpu_x + 4 * cpu_y
          cpu = 2 * cpu_x + 4 * cpu_y
          # Hasil Perkalian Persamaan 2(GPU) -> gpu = 12 * gpu_x + 4 * gpu_y
          gpu = 12 * gpu_x + 4 * gpu_y
          
          # Pengoperasian variabel y Pada Persamaan CPU dan GPU
          # Karena variebal y hasilnya 0 kita hanya sisa mencari nilai variabel x nya
          y_cpu_gpu = (4 * cpu_y) - (4 * gpu_y)
          print(f"Hasil Pengoperasian Persamaan Pada Variabel y: {y_cpu_gpu}")
          
          x_cpu_gpu = (2 * cpu_x) - (12 * gpu_x)
          print(f"Hasil Pengoperasian Persamaan Pada Variabel x: {x_cpu_gpu}")
          
          constant_x_val = constant_cpu_val - constant_gpu_val
          print(f"Hasil Pengoperasian Konstanta Antar 2 Persamaan: {constant_x_val}")
          x = constant_x_val / x_cpu_gpu
          
          # Hasil Akhir Mencari Nilai Variabel X adalah 14
          print(f"Hasil Akhir Mencari Nilai Variabel x: {round(x)}")
          print("=" * 67, "\n")
          
          # Mencari Nilai Y 
          print(f"{"=" * 10} {"mencari nilai variabel y pada kedua persamaan".upper()} {"=" * 10}")
          
          # Persamaan 1(CPU): cpu = 2 * cpu_x + 4 * cpu_y
          cpu = (2 * cpu_x * 3) + (4 * cpu_y * 3)
          constant_cpu_val = 100 * 3
          # Persamaan 2(GPU): gpu = 3 * gpu_x + gpu_y
          gpu = (3 * gpu_x * 2) + (gpu_y * 2)
          constant_gpu_val = 60 * 2
          
          # Hasil Perkalian Persamaan 1(CPU) -> cpu = 6 * cpu_x + 12 * cpu_y
          cpu = 6 * cpu_x + 12 * cpu_y
          # Hasil Perkalian Persamaan 2(GPU) -> gpu = 6 * gpu_x + 2 * gpu_y
          gpu = 6 * gpu_x + 2 * gpu_y
          
          # Pengoperasian variabel x Pada Persamaan CPU dan GPU
          # Karena variebal x hasilnya 0 kita hanya sisa mencari nilai variabel y nya
          y_cpu_gpu = (12 * cpu_y) - (2 * gpu_y)
          print(f"Hasil Pengoperasian Persamaan Pada Variabel y: {y_cpu_gpu}")
          
          x_cpu_gpu = (6 * cpu_x) - (6 * gpu_x)
          print(f"Hasil Pengoperasian Persamaan Pada Variabel x: {x_cpu_gpu}")
          
          constant_y_val = constant_cpu_val - constant_gpu_val
          print(f"Hasil Pengoperasian Konstanta Antar 2 Persamaan: {constant_y_val}")
          
          y = constant_y_val / y_cpu_gpu
          # Hasil Akhir Mencari Nilai Variabel X adalah 14
          print(f"Hasil Akhir Mencari Nilai Variabel y: {round(y)}")
          print("=" * 67, "\n")
          
          # Hasil Akhir Dari Kedua Persamaan
          print(f"{"=" * 10} {"hasil akhir kedua persamaan".upper()} {"=" * 10}")
          
          equation_cpu = 2 * x + 4 * y
          equation_gpu = 3 * x + y
          print(f"Hasil Akhir Persamaan CPU: {round(equation_cpu)}\nHasil Akhir Persamaan GPU: {round(equation_gpu)}")
          print("=" * 49, "\n")

computing_resource_allocation(cpu_x=1, cpu_y=1, gpu_x=1, gpu_y=1)