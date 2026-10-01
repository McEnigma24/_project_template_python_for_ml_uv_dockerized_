"""Domyślny punkt wejścia w kontenerze: run_main"""

from __future__ import annotations

import os
from datetime import datetime


def main() -> None:
    log_root = os.environ.get("TENSORBOARD_LOGDIR", "/workspace/runs")
    run_dir = os.path.join(log_root, datetime.now().strftime("%Y%m%d-%H%M%S"))

    print("ML template — main.py")
    try:
        import torch
        from torch.utils.tensorboard import SummaryWriter

        print(f"PyTorch {torch.__version__}, CUDA: {torch.cuda.is_available()}")
        writer = SummaryWriter(log_dir=run_dir)
        for step in range(10):
            writer.add_scalar("demo/loss", 1.0 / (step + 1), step)
        writer.close()
        print(f"TensorBoard logi: {run_dir}  (w shellu: tb)")
    except ImportError:
        print("Brak torch — uruchom na hoście: ./scripts/drun sync")


if __name__ == "__main__":
    main()
