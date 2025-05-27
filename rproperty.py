# Tagle, Marc Neil V.

class Relation_Property_Checker: # IMPORTANTE: Gumagawa po ito ng isang class na tinawag na 'Relation Property Checker'.

    def __init__(self) -> None: # Ito po ang constructor ng class.
        pass # Wala pong attributes ang ating class.


    def show_title(self) -> None: # Gumagawa po ito ng isang function na tinawag na 'show_title'.
        print("--- RELATION PROPERTY CHECKER ---") # Pini-print po nito ang title ng program sa terminal.


    def get_set(self) -> list: # IMPORTANTE: Gumagawa po ito ng isang function na tinawag na 'get_set'.
        print("CREATE SET") # Pini-print po nito ang title ng menu ng paggawa ng set.
        print("Enter elements of your set.") # Pini-print po nito ang instructions sa paggawa ng set.
        print("Enter blank to proceed.\n") # Kapag tapos na po mag-enter ng elements, magp-press [Enter] nalang to proceed.
        
        s = [] # Ini-initialize po nito ang isang list para sa ating set.
        i = 1 # Ini-initialize po nito ang index para malaman kung pang-ilan na element na ang ine-enter.
        while True: # Gumagawa po ito ng isang while loop na umiikot habang hindi pa bini-break.
            element = input(f"Enter element {i}: ").strip() # Humihingi po ito ng element kay user kada iteration.

            if element == '': # Ni-che-check po nito kung ang ni-input ni user ay blank.
                break # Kapag blanko po ang ni-input ni user, ang while loop ay magb-break.

            if element not in s: # Ni-che-check po nito kung ang ni-input ni user ay wala sa list 's'.
                s.append(element) # Kapag wala po sa list 's' ang input, ito ay i-a-append sa list.
                i += 1 # Pagkatapos po i-append ang bagong element, i-i-increment ang index para sa kasunod na prompt.
            else: # Kapag hindi po nasatisfy ang kanyang if condition, ang sumusunod na code ang magru-run.
                print("Element already in set.") # Kapag ang ni-input po si user ay naka'y list 's' na, ito ang i-pi-print sa terminal.
        
        s.sort() # Ni-o-organize po nito si list 's' upang mas maging maayos tingnan 'pag ni-print ito sa terminal.
        return s # Nire-return po ng function na ito ang list 's'.
    

    def show_set(self, s) -> None: # Gumagawa po ito ng isang function na tinawag na 'show_set'.
        print(f"A = {{{', '.join(s)}}}") # Ni-pi-print po nito ang list 's' sa format na 'A = {a, b, c, ...}'.


    def get_relation(self, s) -> list: # IMPORTANTE: Gumagawa po ito ng isang function na tinawag na 'get_relation'.
        print("CREATE RELATION") # Pini-print po nito ang title ng menu ng paggawa ng relation.
        print("Enter ordered pairs of elements from your set in the format (a,b).") # Pini-print po nito ang instructions sa paggawa ng relation.
        print("Enter blank to proceed.\n") # Kapag tapos na po mag-enter ng pairs, magp-press [Enter] nalang to proceed.
        self.show_set(s) # Tinatawag po nito ang function na 'show_set' para ipakita sa user ang elements ng kanyang set.
        print() # Ito po ay for terminal-based UI purposes.

        r = [] # Ini-initialize po nito ang isang list para sa ating relation.
        i = 1 # Ini-initialize po nito ang index para malaman kung pang-ilan na pair na ang ine-enter.
        while True: # Gumagawa po ito ng isang while loop na umiikot habang hindi pa bini-break.
            pair = input(f"Enter pair {i}: ").strip() # Humihingi po ito ng isang pair kay user kada iteration.

            if pair == '': # Ni-che-check po nito kung ang ni-input ni user ay blank.
                break # Kapag blanko po ang ni-input ni user, ang while loop ay magb-break.

            if pair.startswith('(') and pair.endswith(')'): # Ni-che-check po nito kung nasa tamang format ang ni-enter ni user.
                elements = pair[1:-1].split(',') # Tinatanggal po nito ang parentheses para ma-access ang mismong a and b pair.
                if len(elements) == 2: # Ni-che-check po nito kung ang pair ay binary o may dalawang elements lamang.
                    a, b = elements[0].strip(), elements[1].strip() # Ni-e-extract po nito ang dalawang elements sa variables na a, b
                    if a in s and b in s: # Ni-che-check po nito kung si a at b ay elements ng set.
                        if (a,b) in r: # Ni-che-check po nito kung ang pair ay nasa list 'r' already.
                            print("Pair already in relation.") # Kapag nag-e-exist na po ang pair kay list 'r', ito po ang i-pi-print.
                        else: # Kapag hindi po nasatisfy ang kanyang if condition, ang sumusunod na code ang magru-run.
                            r.append((a, b)) # Kapag wala po sa list 'r' ang input, ito ay i-a-append sa list.
                            i += 1 # Pagkatapos po i-append ang bagong element, i-i-increment ang index para sa kasunod na prompt.
                    else: # Kapag hindi po nasatisfy ang kanyang if condition, ang sumusunod na code ang magru-run.
                        print("Element/s not in set.") # Kapag isa o parehas na elements ay wala sa set, ito po ang i-pi-print.
                else: # Kapag hindi po nasatisfy ang kanyang if condition, ang sumusunod na code ang magru-run.
                    print("Invalid pair format. Use (a,b).") # Kapag hindi po binary ang relation, ito po ang i-pi-print.
            else: # Kapag hindi po nasatisfy ang kanyang if condition, ang sumusunod na code ang magru-run.
                print("Invalid pair format. Use (a,b).") # Kapag hindi po naka-enclosed in parentheses ang pair, ito po ang i-pi-print.
        
        r.sort() # Ni-o-organize po nito si list 'r' upang mas maging maayos tingnan 'pag ni-print ito sa terminal.
        return r # Nire-return po ng function na ito ang list 'r'.
    

    def show_relation(self, r) -> None: # Gumagawa po ito ng isang function na tinawag na 'show_relation'.
        formatted_pairs = ', '.join(f'({a},{b})' for a, b in r) # Ni-co-comma separate po nito ang bawat pair kay list 'r'.
        print(f"R = {{{formatted_pairs}}}") # Ni-pi-print po nito ang list 'r' sa format na 'R = {(a,b), (c,d), ...}'.


    def is_reflexive(self, s, r) -> bool: # IMPORTANTE: Gumagawa po ito ng isang function na tinawag na 'is_reflexive'.
        for e in s: # Gumagawa po ito ng isang for loop na nag-i-iterate sa list 's' (ang ating set).
            if (e,e) not in r: # Ni-che-check po nito kung ang self-pair ng isang element ng set ay wala sa relation.
                return False # Kung wala po ang self-pair sa relation, i-re-return po ng function ay False.
        return True # Kapag lahat po ng self-pairs ng bawat set element ay nasa relation, i-re-return ng function ay True.


    def is_symmetric(self, r) -> bool: # IMPORTANTE: Gumagawa po ito ng isang function na tinawag na 'is_symmetric'.
        for a, b in r: # Gumagawa po ito ng isang for loop na nag-i-iterate sa list 'r' (ang ating relation).
            if (b, a) not in r: # Ni-che-check po nito kung ang symmetric-pair ng isang pair ay wala sa relation.
                return False # Kung wala pong symmetric pair ang isang pair sa relation, i-re-return po ng function ay False.
        return True # Kapag lahat po ng pair sa relation ay may symmetric pair, i-re-return ng function ay True.


    def is_antisymmetric(self, r) -> bool: # IMPORTANTE: Gumagawa po ito ng isang function na tinawag na 'is_antisymmetric'.
        for a, b in r:  # Gumagawa po ito ng isang for loop na nag-i-iterate sa list 'r' (ang ating relation).
            if (b, a) in r and a != b: # Ni-che-check po nito kung ang symmetric-pair ng isang pair ay nasa sa relation at ang magka-pair ay equal sa isa't isa.
                return False # Kapag may magka-symmetric po na pair sa relation at ang elements ng pairs ay hindi equal sa isa't isa, i-re-return ng function ay False.
        return True # Kapag wala pong nakitang nagsatify sa condition ng if block, i-re-return ng function ay True.


    def is_transitive(self, r) -> bool: # IMPORTANTE: Gumagawa po ito ng isang function na tinawag na 'is_transitive'.
        for a, b in r: # Kumukuha po ito ng bawat pares mula sa r at itatalaga sa a at b sa bawat ikot kay list 'r'.
            for c, d in r: # Kumukuha po ito ng bawat pares mula sa r at itatalaga naman sa c at d sa bawat ikot kay list 'r'.
                if b == c and (a, d) not in r: # Ni-che-check po nito kung may transitive chain ba na nasira.
                    return False # If me'ron pong transitive chain ang nasira o hindi kumpleto, i-re-return ng function ay False.
        return True # If wala pong transitive chain na hindi kumpleto, i-re-return ng function ay True.
    
    def show_properties(self, s, r) -> None: # Gumagawa po ito ng isang function na tinawag na 'show_properties'.
        print("RELATION PROPERTIES") # Pini-print po nito ang header bago ipakita ang properties ng relation. 
        print(f"Reflexive: {'Yes' if self.is_reflexive(s, r) else 'No'}") # Pinapakita po nito kung reflexive ang relation o hindi.
        print(f"Symmetric: {'Yes' if self.is_symmetric(r) else 'No'}") # Pinapakita po nito kung symmetric ang relation o hindi.
        print(f"Antisymmetric: {'Yes' if self.is_antisymmetric(r) else 'No'}") # Pinapakita po nito kung antisymmetric ang relation o hindi.
        print(f"Transitive: {'Yes' if self.is_transitive(r) else 'No'}") # Pinapakita po nito kung transitive ang relation o hindi.