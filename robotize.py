"""
Simple I/O wire example, connecting the input directly to the output
This example uses the default PortAudio API, however you can change it by
using the "api" keyword argument in AudioIO creation, like
  with AudioIO(True, api="jack") as pr:
obviously, you can use another API instead (like "alsa").
Note
----
When using JACK, keep chunks.size = 1
"""

from audiolazy import chunks, AudioIO
import sys

# Choose API via command-line
api = sys.argv[1] if sys.argv[1:] else None

# Amount of samples per chunk to be sent to PortAudio
chunks.size = 1 if api == "jack" else 16

with AudioIO(True, api=api) as pr: # A player-recorder
  pr.play(pr.record())