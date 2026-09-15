# GestureBot

Early prototype: hand-presence/pose detection using Meta's InterHand2.6M model, aimed at gesture-controlled robotics.

## What it is

An early proof-of-concept. It loads a pretrained [InterHand2.6M](https://github.com/facebookresearch/InterHand2.6M)
checkpoint (a hand pose estimation model, included as a git submodule) and runs it on a static test
image to detect whether a left and/or right hand is present.

It does not yet do real-time video, gesture classification, or control anything — the "robot" side
of gesture-controlled robotics is planned, not built yet.

## Stack

- Python, PyTorch, OpenCV
- InterHand2.6M (submodule)

## Status

Early prototype / proof of concept.

## Running it

The InterHand2.6M model checkpoint (`snapshot_20.pth.tar`, ~540MB) is not committed to this repo
(it exceeds GitHub's file size limit). Download it from the
[InterHand2.6M releases](https://github.com/facebookresearch/InterHand2.6M) and place it at the
repo root before running:

```bash
python main.py
```
