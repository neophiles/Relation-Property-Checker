# Tagle, Marc Neil V.

from rproperty import Relation_Property_Checker # Ni-i-import po nito ang module/class na 'Relation_Property_Checker' sa file na 'rproperty'.
import os # Ni-i-import po nito ang 'os' module para sa purpose ng pagclear ng terminal.

def divider() -> None: # Gumagawa po ito ng isang function na tinawag na 'divider'.
    print("_" * 33, "\n") # Naqpi-print po ito ng divider na gawa sa mga underscores. Ito ay for terminal-based UI purposes.

def main() -> None: # Ginagawa po nito ang main function na magiging entry point ng user.
    rpc = Relation_Property_Checker() # Gumagawa po ito ng isang instance ng ating 'Relation_Property_Checker' class.

    while True: # Gumagawa po ito ng isang while loop na umiikot habang hindi pa bini-break.

        while True: # Gumagawa po ito ng isang while loop na umiikot habang hindi pa bini-break.
            rpc.show_title() # Tinatawag po nito ang function na 'show_title' para ipakita ang title ng program sa terminal.
            divider() # Tinatawag po nito ang function na 'divider' para magprint ng divider sa terminal.
            s = rpc.get_set() # Tinatawag po nito ang function na 'get_set' para gumawa si user ng set at ito ay itatalaga kay variable 's'.

            divider() # Tinatawag po nito ang function na 'divider' para magprint ng divider sa terminal.
            while True: # Gumagawa po ito ng isang while loop na umiikot habang hindi pa bini-break.
                proceed = input("Are you happy with your set? [y/n]: ") # Tinatanong po nito ang user kung gusto na niyang magproceed sa paggawa ng relation.
                if proceed == 'y': # Ni-che-check po nito kung ang response ni user ay 'y'.
                    os.system('cls') # Ni-c-clear po nito ang terminal.
                    break # Lalabas po sa inner loop gamit itong keyword.
                elif proceed == 'n': # Ni-che-check po nito kung ang response ni user ay 'n'.
                    os.system('cls') # Ni-c-clear po nito ang terminal.
                    break # Lalabas po sa inner loop gamit itong keyword.
                else: # Ni-che-check po nito kung ang response ni user ay hindi 'y' o 'n'.
                    print("Invalid response! Please enter [y/n].\n") # Ni-pi-print po ito kapag mali ang response ng user.

            if proceed == 'y': # Ni-che-check po nito kung ang response ni user ay 'y'.
                break # Lalabas po sa outer loop gamit itong keyword.
            
        while True: # Gumagawa po ito ng isang while loop na umiikot habang hindi pa bini-break.
            rpc.show_title() # Tinatawag po nito ang function na 'show_title' para ipakita ang title ng program sa terminal.
            divider() # Tinatawag po nito ang function na 'divider' para magprint ng divider sa terminal.
            r = rpc.get_relation(s) # Tinatawag po nito ang function na 'get_relation' para gumawa si user ng relation at ito ay itatalaga kay variable 'r'.

            divider() # Tinatawag po nito ang function na 'divider' para magprint ng divider sa terminal.
            while True: # Gumagawa po ito ng isang while loop na umiikot habang hindi pa bini-break.
                proceed = input("Are you happy with your relation? [y/n]: ") # Tinatanong po nito ang user kung gusto na niyang makita ang properties ng relation.
                if proceed == 'y': # Ni-che-check po nito kung ang response ni user ay 'y'.
                    os.system('cls') # Ni-c-clear po nito ang terminal.
                    break # Lalabas po sa inner loop gamit itong keyword.
                elif proceed == 'n': # Ni-che-check po nito kung ang response ni user ay 'n'.
                    os.system('cls') # Ni-c-clear po nito ang terminal.
                    break # Lalabas po sa inner loop gamit itong keyword.
                else: # Ni-che-check po nito kung ang response ni user ay hindi 'y' o 'n'.
                    print("Invalid response! Please enter [y/n].\n") # Ni-pi-print po ito kapag mali ang response ng user.

            if proceed == 'y': # Ni-che-check po nito kung ang response ni user ay 'y'.
                break # Lalabas po sa outer loop gamit itong keyword.

        rpc.show_title() # Tinatawag po nito ang function na 'show_title' para ipakita ang title ng program sa terminal.
        divider() # Tinatawag po nito ang function na 'divider' para magprint ng divider sa terminal.
        rpc.show_set(s) # Tinatawag po nito ang function na 'show_set' para ipakita ang nakaformat na set sa terminal.
        rpc.show_relation(r) # Tinatawag po nito ang function na 'show_relation' para ipakita ang nakaformat na relation sa terminal.
        print() # Ito po ay for terminal-based UI purposes.
        rpc.show_properties(s, r) # Tinatawag po nito ang function na 'show_properties' para ipakita ang mga properties ng relation.
        divider() # Tinatawag po nito ang function na 'divider' para magprint ng divider sa terminal.

        while True: # Gumagawa po ito ng isang while loop na umiikot habang hindi pa bini-break.
            another = input("Do you want to check the properties of another relation? [y/n]: ") # Tinatanong po nito ang user kung gusto niyang ulitin ang program.
            if another == 'y': # Ni-che-check po nito kung ang response ni user ay 'y'.
                os.system('cls') # Ni-c-clear po nito ang terminal.
                break # Lalabas po sa loop gamit itong keyword.
            elif another == 'n': # Ni-che-check po nito kung ang response ni user ay 'n'.
                print("\nProgram by M002 | Tagle, Marc Neil V.") # Ito po ay credits sa gumawa ng program.
                print("Thank you! Goodbye.") # Ito po ang parting message ng program.
                return # Kapag hindi na gusto ng user na magcheck ng isa pang relation, mag-re-return ang 'main' function at matatapos ang pagrun ng program.
            else: # Ni-che-check po nito kung ang response ni user ay hindi 'y' o 'n'.
                print("Invalid response! Please enter [y/n].\n") # Ni-pi-print po ito kapag mali ang response ng user.

if __name__ == '__main__': # Kapag ang pangalan po ng file ay 'main', magru-run ang sumusunod na function.
    main() # Tinatawag po nito ang 'main' function at magsisimula at program.