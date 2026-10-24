import random
from rich import print
from rich.panel import Panel
from rich.table import Table

def seleccionarpokemon():
    print(Panel("[bold yellow]===== SELECCIONA TU POKÉMON =====[/bold yellow]"))
    print("[bold red]1. Charmander[/bold red]  (vida: 100, ataque máx: 25)")
    print("[bold cyan]2. Squirtle[/bold cyan]    (vida: 120, ataque máx: 20)")
    print("[bold green]3. Bulbasaur[/bold green]   (vida: 110, ataque máx: 22)\n")
    
    while True:
        opcion = input("Elige tu Pokémon (1-3): ")
        
        if opcion == "1":
            nombre = "Charmander"
            vida = 100
            ataque = 25
            break
        elif opcion == "2":
            nombre = "Squirtle"
            vida = 120
            ataque = 20
            break
        elif opcion == "3":
            nombre = "Bulbasaur"
            vida = 110
            ataque = 22
            break
        else:
            print("[bold red]Opción no válida. Intenta de nuevo.[/bold red]")
            
    return nombre, vida, ataque

def seleccionarrival():
    numero = random.randint(1, 3)
    
    if numero == 1:
        nombrerival = "Charmander"
        vidarival = 100
        ataquerival = 25
    elif numero == 2:
        nombrerival = "Squirtle"
        vidarival = 120
        ataquerival = 20
    else:
        nombrerival = "Bulbasaur"
        vidarival = 110
        ataquerival = 22
        
    return nombrerival, vidarival, ataquerival

def mostrarmenu():
    print(Panel("[bold magenta]===== BATALLA POKÉMON =====[/bold magenta]"))
    print("[bold red]1. Atacar[/bold red]")
    print("[bold green]2. Curarse[/bold green]")
    print("[bold cyan]3. Ver estado[/bold cyan]")
    print("[bold yellow]4. Huir[/bold yellow]")
    return input("Elige una opción: ")

def atacar(nomj, atkmaxj, nomr, hpr):
    dano = random.randint(10, atkmaxj)
    hpr = hpr - dano
    if hpr < 0:
        hpr = 0
    print(f"\n[bold green]⚔️  {nomj}[/bold green] ataca a [bold red]{nomr}[/bold red] y le causa [bold red]{dano} de daño[/bold red]")
    return hpr

def contraatacarrival(nomr, nomj, hpj):
    danorival = random.randint(5, 20)
    hpj = hpj - danorival
    if hpj < 0:
        hpj = 0
    print(f"[bold red]💥 {nomr}[/bold red] contraataca a [bold green]{nomj}[/bold green] y le causa [bold red]{danorival} de daño[/bold red]\n")
    return hpj

def curarse(hpj, maxj, curaciones):
    if curaciones <= 0:
        print("\n[bold red]❌ Ya no tienes curaciones disponibles[/bold red]\n")
        return hpj, curaciones
    
    if hpj == maxj:
        print("\n[bold yellow]⚠️  Tu Pokémon ya tiene la vida al máximo[/bold yellow]\n")
        return hpj, curaciones

    hpj = hpj + 20
    if hpj > maxj:
        hpj = maxj
        
    curaciones = curaciones - 1
    print(f"\n[bold green]💖 Te has curado. Vida actual: {hpj}/{maxj}[/bold green]\n")
    return hpj, curaciones

def meostrarestado(nomj, hpj, maxj, nomr, hpr, maxr, curaciones):
    tabla = Table(title="ESTADO DE BATALLA")
    tabla.add_column("Entrenador", style="bold")
    tabla.add_column("Pokémon", style="cyan")
    tabla.add_column("Vida", style="green")

    tabla.add_row("Tú", nomj, f"{hpj}/{maxj}")
    tabla.add_row("Rival", nomr, f"{hpr}/{maxr}")

    print("\n", tabla)
    print(f"[bold yellow]🧪 Curaciones restantes: {curaciones}[/bold yellow]\n")

# --- INICIO DEL JUEGO ---
nombrej, vidamaxj, ataquemaxj = seleccionarpokemon()
vidaj = vidamaxj

nombrer, vidamaxr, ataquemaxr = seleccionarrival()
vidar = vidamaxr

curaciones = 3
enbatalla = True

print(Panel(f"[bold red]¡Un {nombrer} salvaje ha aparecido![/bold red]", title="¡ALERTA!"))

while enbatalla:
    opcion = mostrarmenu()
    
    if opcion == "1":
        vidar = atacar(nombrej, ataquemaxj, nombrer, vidar)
        
        if vidar == 0:
            print(Panel("[bold green]🏆 ¡VICTORIA! Has derrotado al Pokémon rival.[/bold green]"))
            enbatalla = False
        else:
            vidaj = contraatacarrival(nombrer, nombrej, vidaj)
            if vidaj == 0:
                print(Panel("[bold red]💀 DERROTA... Tu Pokémon ha caído.[/bold red]"))
                enbatalla = False
                
    elif opcion == "2":
        vidaj, curaciones = curarse(vidaj, vidamaxj, curaciones)
        
    elif opcion == "3":
        meostrarestado(nombrej, vidaj, vidamaxj, nombrer, vidar, vidamaxr, curaciones)
        
    elif opcion == "4":
        print(Panel("[bold yellow]🏃 Has escapado de la batalla.[/bold yellow]"))
        enbatalla = False
        
    else:
        print("\n[bold red]Opción inválida. Elige un número del 1 al 4.[/bold red]\n")