import simpy
import random
import numpy as np
import matplotlib.pyplot as plt

# Configuración de la simulación
RANDOM_SEED = 42 # Semilla para reproducibilidad
NUM_PROCESSES = [25, 50, 100, 150, 200] # Número de procesos a simular
INTERVALS = [10, 5, 1] # Intervalos de llegada de procesos
MEM_CAPACITY = 100 # Capacidad de memoria RAM
INSTRUCTIONS_PER_TIME = 3 # Instrucciones ejecutadas por unidad de tiempo
CPU_SPEED = 1  # Unidades de tiempo por instrucción
MEMORY_SPEED = 1  # Unidades de tiempo por memoria
WAIT_PROBABILITY = 0.5 # Probabilidad de esperar por E/S
INTERVAL = 10

class Process:
    def __init__(self, env, name, cpu, memory):
        self.env = env
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.instructions_remaining = random.randint(1, 10)

    def run(self):
        while self.instructions_remaining > 0:
            # Solicitar acceso al CPU
            with self.cpu.request() as req:
                # Ejecutar instrucciones en el CPU
                yield req
                instructions_to_execute = min(self.instructions_remaining, INSTRUCTIONS_PER_TIME)
                yield self.env.timeout(instructions_to_execute * CPU_SPEED)
                self.instructions_remaining -= instructions_to_execute

                if self.instructions_remaining <= 0:
                    break

                # Simular E/S (entrada/salida)
                io_wait = random.random()
                if io_wait <= WAIT_PROBABILITY:
                    yield self.env.timeout(random.randint(1, 2))
                else:
                    yield self.env.timeout(0)


def process_generator(env, cpu, ram):
    process_id = 0
    while True:
        yield env.timeout(random.expovariate(1.0 / INTERVAL))
        process_id += 1
        # Solicitar memoria RAM
        mem_required = random.randint(1, 10)
        if mem_required <= ram.level:
            ram.get(mem_required)
            # Crear nuevo proceso
            p = Process(env, f"Process_{process_id}", cpu, ram)
            env.process(p.run())


def simulate(num_processes, interval):
    env = simpy.Environment()
    random.seed(RANDOM_SEED)
    cpu = simpy.Resource(env, capacity=1)
    ram = simpy.Container(env, init=MEM_CAPACITY, capacity=MEM_CAPACITY)
    # Ejecutar generador de procesos
    env.process(process_generator(env, cpu, ram))
    env.run(until=num_processes * interval)

    return env.now / num_processes  # Average time per process


def run_simulation():
    results = {}
    for interval in INTERVALS:
        avg_times = []
        for num_processes in NUM_PROCESSES:
            avg_time = simulate(num_processes, interval)
            avg_times.append(avg_time)
            print(f"Tiempo promedio de {num_processes} procesos e intervalos de {interval}: {avg_time}")

        results[interval] = avg_times

    return results

# Función para graficar los resultados
def plot_results(results):
    for interval, avg_times in results.items():
        plt.plot(NUM_PROCESSES, avg_times, label=f"Interval {interval}")

    plt.title('Tiempo promedio vs Número de procesos')
    plt.xlabel('Número de procesos')
    plt.ylabel('Tiempo Promedio')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    # Ejecutar simulación y graficar resultados
    simulation_results = run_simulation()
    plot_results(simulation_results)