# Sourced by interactive shells (entrypoint bash + docker exec attach).
export PATH="/workspace/bin:/workspace/build/venv/bin:/root/.local/bin:${PATH}"
_extra="${PYTHONPATH_EXTRA:-}"
if [[ -n "${_extra}" ]]; then
  export PYTHONPATH="/workspace:${_extra}"
else
  export PYTHONPATH="/workspace"
fi
