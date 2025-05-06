import asyncio

async def main():
    print("hello")
    await asyncio.sleep(1)
    print("world")

asyncio.run(main())

# The asyncio.run() function to run t
# he top-level entry point “main()” function


#  create task example
import asyncio
import time

async def say_after(delay,what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    task1 = asyncio.create_task(
        say_after(1,"hello")
    )

    task2 = asyncio.create_task(
        say_after(2,"World")
    )

    print(f"started at {time.strftime('%X')}")

    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())


# another example of create_task
import asyncio

async def wait_and_print(str):
  await asyncio.sleep(1)
  print(str)

async def main():
  tasks = []

  for i in range(1, 10):
    tasks.append(asyncio.create_task(wait_and_print(i)))

  for task in tasks:
    await task

asyncio.run(main())


# task group example
import asyncio
import time

async def say_after(delay,what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(
            say_after(1,"hello")
        )
        task2 = tg.create_task(
            say_after(2,"world")
        )
        print(f"started at {time.strftime('%X')}")
    # await is implicity when control exits context manager

    print(f"started at {time.strftime('%X')}")


asyncio.run(main())


# concurrent gather example
mport asyncio
import time

async def factorial(name,number):
    f = 1
    for i in range(2, number+1):
        print(f"Task {name}: Compute factorial{number}, currently i={i}...")
        await asyncio.sleep(1)
        f *= i
    print(f"Task {name}: factorial({number}) = ({f})")
    return f

async def main():
    L = await asyncio.gather(
        factorial('A',2),
        factorial('B',3),
        factorial('C',4),
    )
    print(L)

asyncio.run(main())


