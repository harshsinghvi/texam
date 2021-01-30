import argparse
import queue
import sys
from datetime import datetime
import sounddevice as sd
import numpy  # Make sure NumPy is loaded before it is used in the callback
assert numpy  # avoid "imported but unused" message (W0611)
l=[]
t=[]
count=0

def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text


parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    '-l', '--list-devices', action='store_true',
    help='show list of audio devices and exit')
args, remaining = parser.parse_known_args()
if args.list_devices:
    print(sd.query_devices())
    parser.exit(0)
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser])
parser.add_argument(
    'filename', nargs='?', metavar='FILENAME',
    help='audio file to store recording to')
parser.add_argument(
    '-d', '--device', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-r', '--samplerate', type=int, help='sampling rate')
parser.add_argument(
    '-c', '--channels', type=int, default=1, help='number of input channels')
parser.add_argument(
    '-t', '--subtype', type=str, help='sound file subtype (e.g. "PCM_24")')
args = parser.parse_args(remaining)
q = queue.Queue()


def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())

def P():
    if args.samplerate is None:
        device_info = sd.query_devices(args.device, 'input')
        args.samplerate = int(device_info['default_samplerate'])
    with sd.InputStream(samplerate=args.samplerate, device=args.device,
                        channels=args.channels, callback=callback):
        while True:
            data=q.get()
            for i in data:
                x = int(i[0] * 1000)
                if x < 0:
                        x=(-1 * x)
                    current_time = datetime.now()
                    if current_time not in t:
                        t.append(current_time)
                    if x > 300:
                        if current_time not in l:
                            l.append(current_time)
                    if len(t)==10:
                        if len(l)==8:
                            print("yessss")
                            parser.exit(0)
                        else:
                            print("*")
                            parser.exit(0)
    except Exception as e:
        parser.exit(type(e).__name__ + ': ' + str(e))
while(True):
    P()
