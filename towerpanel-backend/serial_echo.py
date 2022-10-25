import asyncio
import serial_asyncio


async def main(loop):
    reader, writer = await serial_asyncio.open_serial_connection(url='./ttySensor', baudrate=115200)
    print('Writer opened')
    messages = [
        b'TEMP,25,01\n',
        b'TEMP,25,02\n',
        b'TEMP,25,03\n',
        b'TEMP,25,04\n',
        b'TEMP,25,05\n',
        b'TEMP,25,06\n',
        b'TEMP,25,07\n',
        b'TEMP,25,08\n',
        b'TEMP,25,09\n',
        b'TEMP,25,10\n',
        b'TEMP,25,11\n',
        b'TEMP,25,12\n',
        b'TEMP,25,13\n',
        b'TEMP,25,14\n',
        b'TEMP,25,15\n',
        b'TEMP,25,16\n',
        b'TEMP,25,17\n',
        b'TEMP,25,18\n',
        b'TEMP,25,19\n',
        b'TEMP,25,20\n',
    ]
    sent = send(writer, messages)
    received = recv(reader)
    await asyncio.wait([
        asyncio.create_task(sent),
        asyncio.create_task(received),
        ])


async def send(w, msgs):
    while True:
        for msg in msgs:
            w.write(msg)
            print(f'sent: {msg.decode().rstrip()}')
            await asyncio.sleep(0.8)
        w.write(b'DONE\n')
        print(f'sent: DONE')
        await asyncio.sleep(0.8)


async def recv(r):
    while True:
        msg = await r.readuntil(b'\n')
        print(f'received: {msg.rstrip().decode()}')


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main(loop))
    loop.close()
