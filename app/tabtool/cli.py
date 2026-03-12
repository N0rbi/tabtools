from pathlib import Path
from typing import List

import typer

from .controllers import DataRequestController
from .models import Options
from .services import FileService

app = typer.Typer()
fs = FileService()

all_info : bool = typer.Option(False, "--all", "-all")
columns : List[str] = typer.Option(None, "--col", "--column", "-c")
performance_check : bool = typer.Option(False, "--perf", "--performance", "-p")

@app.command()
def main(input_file_name : str, all_info : bool = all_info, 
            columns : List[str] = columns, 
            performance_check : bool = performance_check):
        
        if performance_check:
            raise ValueError("Performance checks are not implemented yet.")

        if all_info and columns:
            raise typer.BadParameter("All info and specific columns cannot be used together")
        
        if (all_info or columns) and performance_check:
            raise typer.BadParameter("Performance check does not allow any other options")

        options = Options(input_file_name, all_info, columns, performance_check)
        file_path : Path = Path(input_file_name).resolve()
        filename = fs.parse_file(file_path)

        if (not fs.exists(file_path)):
            raise ValueError("File does not exist")
        
        DataRequestController.handle_request(filename, options)
        