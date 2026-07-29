import asyncio
import time

async def slow_task(name, seconds):
    print(f"{name} starting")
    await asyncio.sleep(seconds)
    print(f"{name} done")

async def main():
    start = time.time()
    await asyncio.gather(
        slow_task("Task A", 2),
        slow_task("Task B", 2),
        slow_task("Task C", 2)
    )
    print(f"Total time: {time.time() - start:.2f} seconds")

asyncio.run(main())