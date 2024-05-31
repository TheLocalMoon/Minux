#--services.py--#
import importlib.util
import log, importlib
logging = log.pyLOG()

def load_service(dir: str, module_name: str):
    try:
        full_path = f"{dir}/{module_name}"
        logging.none(f"loading {full_path} . . .")
        spec = importlib.util.spec_from_file_location(module_name, full_path)
        if not spec:
            logging.error(f"service {module_name} not found at {full_path}")
            return
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        logging.info(f"loaded {full_path}")
        return module
    except Exception as e:
        logging.error(f"error loading {full_path}: {e}")
        return None