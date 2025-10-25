
import pytest
import sys
import os

def run_all_tests():
    
    
    test_path = 'tests/'
    
   
    args = [
        test_path,
        '-v',
        '--html=reporte.html',
        '--self-contained-html'
    ]

    print("🚀 Iniciando la ejecución de Pytest...")
    
    
    exit_code = pytest.main(args)
    
    if exit_code == 0:
        print("\n✅ EJECUCIÓN EXITOSA. Reporte generado en reporte.html")
    else:
        print(f"\n❌ EJECUCIÓN FALLIDA. Código de salida: {exit_code}")
        
    sys.exit(exit_code)

if __name__ == "__main__":
    run_all_tests()

