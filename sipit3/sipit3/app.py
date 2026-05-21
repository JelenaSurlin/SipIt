from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import yaml
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'supersecretkey'

# Load or create users.yaml
users_file = 'users.yaml'
try:
    with open(users_file, 'r') as file:
        users = yaml.safe_load(file) or {}
except FileNotFoundError:
    users = {}

def save_users():
    with open(users_file, 'w') as file:
        yaml.safe_dump(users, file)

# Flask-Mail configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Replace with your mail server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'mija.vujnovic2@gmail.com'  # Replace with your email
app.config['MAIL_PASSWORD'] = 'wyho ebhm tiqf vtcd'  # Replace with your email password
app.config['MAIL_DEFAULT_SENDER'] = 'mija.vujnovic2@gmail.com'  # Replace with your email

mail = Mail(app)


@app.route('/')
def home():
    if 'username' in session:
        user = session['username']
        # Prikaz za prijavljenog korisnika
    elif 'guest' in session:
        # Prikaz za gosta
        guest_user = True
        return render_template('index.html', guest_user=guest_user)
    else:
        return redirect(url_for('login'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'error')
    return render_template('login.html')




@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username in users:
            flash('Username already exists', 'error')
        else:
            users[username] = password
            save_users()
            flash('Registration successful. You can now log in.', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/index')
def index():
    guest_user = 'guest' in session
    return render_template('index.html', guest_user=guest_user)

@app.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('guest', None)
    return redirect(url_for('login'))


@app.route('/guest')
def guest():
    session['guest'] = True  # Postavlja gost sesiju
    session.pop('username', None)  # Uklanja korisničku sesiju ako postoji
    return redirect(url_for('index'))  # Preusmjerava na početnu stranicu

@app.route('/continue_as_guest')
def continue_as_guest():
    session['guest'] = True
    return redirect(url_for('index'))

# Routes for other pages
@app.route('/recipes')
def recipes():
    return render_template('recipes.html')

@app.route('/barovi')
def barovi():
    return render_template('barovi.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/blog')
def blog():
    articles = {
        1: {'title': 'Top 10 koktela za ovu zimu', 'image': 'winter-cocktails.jpg'},
        2: {'title': 'Kokteli za početnike', 'image': 'beginner-cocktails.jpg'},
        3: {'title': 'Tajne martinija', 'image': 'martini-secrets.jpg'},
        4: {'title': 'Povijest koktela', 'image': 'cocktail-history.jpg'},
        5: {'title': 'Savjeti za bariste', 'image': 'bar-tips.jpg'},
        6: {'title': 'Kokteli za praznike', 'image': 'holiday-cocktails.jpg'},
    }
    return render_template('blog.html', articles=articles)

@app.route('/lokacija')
def lokacija():
    return render_template('lokacija.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog/<int:article_id>')
def blog_post(article_id):
    articles = {
        1: {
        'title': 'Top 10 koktela za ovu zimu',
        'image': 'winter-cocktails.jpg',
        'content': '''
            <p>Zima je savršeno vrijeme za opuštanje uz tople i aromatične koktele koji će ugrijati vaše ruke i srce...</p>

            <h3>1. Vrući toddy</h3>
            <p>Klasični zimski koktel savršen za hladne večeri...</p>
            <img src="/static/Images/hot-toddy.jpg" alt="Vrući toddy" />

            <h3>2. Irish Coffee</h3>
            <p>Spoj toplog napitka i alkohola, Irish Coffee se sastoji od kave, irskog viskija, šećera i šlaga. Idealan je za ljubitelje kave tijekom zimskih dana.</p>
            <img src="/static/Images/irish-coffee.jpg" alt="Irish Coffee" />

            <h3>3. Eggnog</h3>
            <p>Tradicija tijekom blagdana, eggnog je bogat i kremast napitak s jajima, mlijekom, vrhnjem, šećerom i začinima poput muškatnog oraščića. Za odrasle, dodajte rum ili burbon.</p>
            <img src="/static/Images/eggnog.jpg" alt="Eggnog" />

            <h3>4. Mulled Wine (kuhano vino)</h3>
            <p>Zima nije potpuna bez kuhanog vina! Kombinacija crnog vina, klinčića, cimeta, naranče i meda stvara savršen napitak za blagdansko raspoloženje.</p>
            <img src="/static/Images/mulled-wine.jpg" alt="Kuhano vino" />

            <h3>5. Winter Sangria</h3>
            <p>Sangria nije samo za ljeto! Kombinacija crnog vina, soka od naranče, jabuka, krušaka i začina čini ovu zimsku verziju osvježavajuće, ali i tople note.</p>
            <img src="/static/Images/winter-sangria.jpg" alt="Zimska sangria" />

            <h3>6. Chai Whiskey Punch</h3>
            <p>Začinjeni chai čaj u kombinaciji s viskijem, medom i limunom savršeno zagrijava tijekom hladnih dana. Jednostavan za pripremu i prepun okusa.</p>
            <img src="/static/Images/chai-whiskey.jpg" alt="Chai Whiskey Punch" />

            <h3>7. Snowball</h3>
            <p>Retro klasik s likerom od jaja (advokatom), limunadom i ledom. Lagano i osvježavajuće, savršeno za svečane prilike.</p>
            <img src="/static/Images/snowball.jpg" alt="Snowball" />

            <h3>8. Pecan Pie Martini</h3>
            <p>Savršen desertni koktel inspiriran omiljenim zimskim kolačem. Mješavina votke, irskog likera i sirupa od karamele stvara bogat i sladak napitak.</p>
            <img src="/static/Images/pecan-martini.jpg" alt="Pecan Pie Martini" />

            <h3>9. Spiced Rum Hot Chocolate</h3>
            <p>Vruća čokolada za odrasle! Dodajte začinjeni rum i malo cimeta u svoju klasičnu toplu čokoladu za poseban doživljaj.</p>
            <img src="/static/Images/spiced-rum-hot-chocolate.jpg" alt="Vruća čokolada s rumom" />

            <h3>10. Cranberry Margarita</h3>
            <p>Zimski preokret na klasičnu margaritu. Dodajte sok od brusnica, malo limete i tekilu za koktel koji donosi blagdanski duh.</p>
            <img src="/static/Images/cranberry-margarita.jpg" alt="Cranberry Margarita" />

            <p>Nadamo se da ćete uživati u pripremi ovih koktela! Bilo da slavite blagdane ili se samo opuštate kod kuće, svaki od ovih recepata savršeno će ugrijati zimsku atmosferu.</p>
        '''
        },
        2: {
        'title': 'Kokteli za početnike',
        'image': 'beginner-cocktails.jpg',
        'content': '''
            <p>Ako ste tek zakoračili u svijet koktela, ne brinite – jednostavni recepti i lako dostupni sastojci omogućuju vam da brzo postanete majstor koktela. Donosimo vam nekoliko klasičnih recepata koji su savršeni za početnike.</p>

            <h3>1. Mojito</h3>
            <p>Mojito je osvježavajući koktel koji se lako priprema. Trebat će vam bijeli rum, svježa metvica, šećer, sok od limete i gazirana voda. Zgnječite metvicu i šećer, dodajte rum, sok od limete i led, a zatim dolijte gaziranu vodu.</p>
            <img src="/static/Images/mojito.jpg" alt="Mojito" />

            <h3>2. Gin Tonic</h3>
            <p>Jedan od najjednostavnijih koktela! Kombinirajte gin i tonic vodu u omjeru koji vam odgovara. Dodajte krišku limuna ili limete za završni dodir.</p>
            <img src="/static/Images/gin-tonic.jpg" alt="Gin Tonic" />

            <h3>3. Cuba Libre</h3>
            <p>Kombinacija bijelog ruma, Coca-Cole i soka od limete savršena je za početnike. Poslužite s ledom i kriškom limete za dodatnu svježinu.</p>
            <img src="/static/Images/cuba-libre.jpg" alt="Cuba Libre" />

            <h3>4. Aperol Spritz</h3>
            <p>Aperol Spritz je jednostavan i elegantan koktel. Trebat će vam Aperol, pjenušavo vino (poput Prosecca) i soda voda. Poslužite s kriškom naranče.</p>
            <img src="/static/Images/aperol-spritz.jpg" alt="Aperol Spritz" />

            <h3>5. Vodka Soda</h3>
            <p>Minimalistički koktel idealan za početnike. Kombinirajte votku i gaziranu vodu s dodatkom kriške limete ili limuna.</p>
            <img src="/static/Images/vodka-soda.jpg" alt="Vodka Soda" />

            <h3>6. Tequila Sunrise</h3>
            <p>Spektakularnog izgleda i jednostavne pripreme! Kombinirajte tekilu, sok od naranče i malo grenadina. Poslužite u visokoj čaši s ledom.</p>
            <img src="/static/Images/tequila-sunrise.jpg" alt="Tequila Sunrise" />

            <h3>7. Whiskey Sour</h3>
            <p>Savršena ravnoteža kiselog i slatkog! Potrebni su vam viski, svježi limunov sok i jednostavan sirup (šećer i voda u jednakim omjerima). Protresite sa ledom i poslužite.</p>
            <img src="/static/Images/whiskey-sour.jpg" alt="Whiskey Sour" />

            <p>Uz ovih nekoliko recepata, brzo ćete savladati osnovne vještine i impresionirati svoje goste. Svi kokteli mogu se prilagoditi vašem ukusu dodavanjem manje ili više alkohola, šećera ili limuna. Sretno s pripremom!</p>
        '''
        },
        3: {
        'title': 'Tajne martinija',
        'image': 'martini-secrets.jpg',
        'content': '''
            <p>Martini je jedan od najpoznatijih i najomiljenijih koktela na svijetu. Njegova elegancija, jednostavnost i sofisticiranost čine ga omiljenim izborom za ljubitelje koktela. Iako naizgled jednostavan, martini krije mnoge tajne koje ga čine posebnim.</p>
            <img src="/static/Images/martini.jpg" alt="Martini" />
            <h3>1. Osnovni sastojci</h3>
            <p>Tradicionalni martini priprema se od gina i suhog vermuta, ali moderna verzija često koristi votku umjesto gina. Odnos ova dva sastojka može značajno utjecati na okus, pa je važno pronaći omjer koji vama odgovara.</p>
            

            <h3>2. Suho ili mokro?</h3>
            <p>Suhi martini sadrži vrlo malo vermuta, dok mokri martini ima veći omjer vermuta u odnosu na gin ili votku. Ako volite jači okus alkohola, suhi martini je pravi izbor za vas.</p>
            

            <h3>3. Protresen ili promiješan?</h3>
            <p>Tradicionalno, martini se miješa, ali popularna fraza iz James Bond filmova, "protresen, ne promiješan," učinila je protreseni martini poznatim. Protresanjem se postiže hladniji koktel, ali i blago mutan izgled.</p>
            

            <h3>4. Garnitura</h3>
            <p>Klasični dodatak martiniju je zelena maslina ili uvijena kora limuna. Maslina dodaje slankastu notu, dok limun pruža osvježavajući citrusni miris. Neki ljudi preferiraju i kap soka masline za tzv. "Dirty Martini".</p>
            

            <h3>5. Prilagodba vašem ukusu</h3>
            <p>Jedna od najvećih tajni martinija je prilagodba recepta vašim preferencijama. Eksperimentirajte s različitim markama gina, votke i vermuta, kao i s količinom leda, kako biste stvorili savršeni martini za sebe.</p>
            

            <p>Martini je koktel koji svatko može prilagoditi vlastitom ukusu, a njegova jednostavnost čini ga idealnim za početnike i profesionalce. Bez obzira volite li ga suh, mokar, protresen ili promiješan, martini će vas uvijek osvojiti svojim stilom i okusom.</p>
            '''
        },
        4: {
        'title': 'Povijest koktela',
        'image': 'cocktail-history.jpg',
        'content': '''
            <p>Kokteli imaju bogatu i fascinantnu povijest koja seže nekoliko stoljeća unatrag. Od svojih skromnih početaka kao medicinske infuzije do današnjih dana, kokteli su postali neizostavan dio globalne bar kulture. Evo kako je sve počelo.</p>

            <h3>1. Prvi kokteli</h3>
            <p>Za prve koktele često se spominje 19. stoljeće, iako se tvrdi da su se kombinacije alkohola i začina koristile još u antici. U Americi, u razdoblju nakon američke revolucije, kokteli su počeli postajati popularni. U to doba, kokteli su bili vrlo jednostavni, najčešće kombinacije rakije, začina, šećera i vode.</p>
            

            <h3>2. Prolazak kroz Prohibition (Prohibicija)</h3>
            <p>Jedan od najvažnijih perioda u povijesti koktela bio je tijekom Prohibicije u SAD-u (1920-1933). Iako je alkohol bio zabranjen, kokteli su postali ključni način maskiranja loše kvalitete ilegalnog alkohola. Speakeasy barovi (tajni barovi) postali su popularni, a kokteli su postali simbolom otpora prema zakonu.</p>
            

            <h3>3. Zlatno doba koktela</h3>
            <p>Godine nakon Prohibicije označavale su "Zlatno doba koktela" u Americi. Tokom 1930-ih i 1940-ih, kokteli su postali sofisticiraniji. Barovi su razvili razne koktele koristeći širok spektar alkohola i sastojaka. Tada su nastali kokteli kao što su Martini, Manhattan i Daiquiri, koji su postali standardi u barovima diljem svijeta.</p>
            

            <h3>4. Moderni kokteli</h3>
            <p>U današnjem vremenu kokteli su postali vrlo raznoliki i kreativni. Mixologija, umjetnost stvaranja koktela, doživjela je procvat. Umjetnici za koktele koriste različite tehnike, od infuziranja alkohola do složenih ukrasa, kako bi stvorili jedinstvene i sofisticirane koktele. "Craft kokteli" i kokteli bez alkohola također su postali vrlo popularni.</p>
            

            <h3>5. Kokteli danas</h3>
            <p>Danas kokteli nisu samo pića, oni su način života. Barovi diljem svijeta nude inovativne koktele, a globalne manifestacije poput "Međunarodnog dana koktela" slave kreativnost barmena i ljubitelja koktela. S obzirom na svoj dugi i uzbudljiv razvoj, kokteli su postali kulturni fenomen i nezaobilazan dio mnogih društvenih događanja.</p>
            <img src="/static/Images/modern-cocktail-bar.jpg" alt="Danas kokteli" />

            <p>Povijest koktela nije samo povijest pića, to je priča o kreativnosti, kulturi i evoluciji okusa koja se nastavlja razvijati i danas. Bilo da uživate u klasičnim koktelima ili novim inovacijama, svako piće ima svoje mjesto u bogatoj povijesti koktela.</p>

            '''
        },
        5: {
        'title': 'Savjeti za bariste',
        'image': 'barista-tips.jpg',
        'content': '''
            <p>Biti barista nije samo o pravljenju kave i koktela, već o stvaranju iskustva za svakog gosta. Ako želite postati bolji barista, evo nekoliko savjeta koji će vam pomoći da poboljšate svoje vještine i impresionirate svoje goste:</p>

            <h3>1. Upoznajte svoju opremu</h3>
            <p>Svaki barista treba poznavati svoju opremu – od aparata za espresso do shaker-a za koktele. Uvježbajte pravilno korištenje svih alata kako biste osigurali dosljednost u pripremi pića.</p>

            <h3>2. Odlična priprema</h3>
            <p>Bez obzira pravite li kavu ili koktel, ključ je u pripremi. Prvo, provjerite sve sastojke i opremu prije nego što počnete raditi, kako biste izbjegli nesreće ili neugodnosti tijekom posluživanja.</p>

            <h3>3. Ljubaznost i komunikacija</h3>
            <p>Uvijek se ponašajte ljubazno prema gostima. Razvijanje komunikacijskih vještina pomoći će vam da bolje razumijete njihove želje i pružite im personalizirano iskustvo.</p>
            
            <h3>4. Kreativnost i inovacija</h3>
            <p>Nemojte se bojati eksperimentirati s novim receptima i tehnikama. Ponekad samo jedna promjena u pripremi može stvoriti nevjerojatnu razliku u okusu i prezentaciji pića.</p>
            
            

            <p>Postati vrhunski barista zahtijeva vježbu, znanje i strast prema svom poslu. S ovim savjetima, možete podići svoje vještine na višu razinu i postati omiljeni barista u svakom kafiću ili baru.</p>
            '''
        },
        6: {
        'title': 'Kokteli za praznike',
        'image': 'holiday-cocktails.jpg',
        'content': '''
            <p>Za prazničnu sezonu, kokteli su odličan način da unesete malo veselja u svaku proslavu. Bilo da slavite Božić, Novu godinu ili neki drugi praznik, ovi kokteli će stvoriti savršenu atmosferu. Evo pet odličnih koktela koje možete pripremiti za vaše praznične zabave:</p>

            <h3>1. Eggnog (Jajašca)</h3>
            <p>Ovaj klasični božićni koktel savršen je za hladne zimske večeri. S mješavinom jaja, mlijeka, šećera, vanilije i rum-a, pruža kremast, bogat okus koji podsjeća na prazničnu sezonu.</p>

            <h3>2. Mulled Wine (Začinjeno vino)</h3>
            <p>Začinjeno crno vino s cimetom, klinčićima, narančama i drugim začinima, idealno je za zimske večeri. Savršen je za opuštanje uz pećnicu ili ispod dekice, donoseći mirnu atmosferu praznika.</p>

            <h3>3. Pomegranate Margarita (Granatna margarita)</h3>
            <p>Za nešto malo drugačije, granatna margarita je osvježavajuća i puna okusa, s dodanim slatko-kiselkastim okruglom okusom narandže i granate, koji savršeno odgovara božićnoj sezoni.</p>

            <h3>4. Cranberry Moscow Mule (Brusnica Moscow Mule)</h3>
            <p>Mojito u prazničnom stilu! Kombinacija votke, đumbira, brusnice i limete, ovaj koktel je ukusan i veseo, a odličan je za tople i hladne prazničke zabave.</p>

            <h3>5. Hot Buttered Rum (Vrući maslac rum)</h3>
            <p>Za sve ljubitelje toplih, začinjenih napitaka, vrući maslac rum je pravi izbor. S kombinacijom ruma, maslaca, smeđeg šećera, začina i vruće vode, savršen je koktel za uživanje uz kamin.</p>


            <p>Pripremite ove koktele za svoje praznične zabave i zasigurno ćete oduševiti svoje goste. Svi su jednostavni za pripremu, a njihov bogat okus i miris stvorit će nezaboravnu atmosferu.</p>
            '''
        },
    }
    article = articles.get(article_id, {"title": "Članak nije pronađen", "content": "Ovaj članak ne postoji."})
    return render_template('blog_post.html', article=article)

@app.route('/send_email', methods=['POST'])
def send_email():
    # Uzmi podatke sa forme
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Postavi email poruku
    msg = Message(
        subject="Nova poruka sa kontakt forme",
        recipients=["mija.vujnovic2@gmail.com"],  # Tvoj email
        body=f"Poruka od: {name}\nEmail: {email}\n\nPoruka:\n{message}"
    )
    
    try:
        # Pošalji email
        mail.send(msg)
        return jsonify({"status": "success", "message": "Email successfully sent."}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500




favourites_file = 'favourites.yaml'


def load_favourites():
    try:
        with open(favourites_file, 'r') as file:
            return yaml.safe_load(file) or {}
    except FileNotFoundError:
        return {}
    


#---------------------------------------------


favourites = {}

@app.route('/api/favourites/post', methods=['POST'])
def save_favourites():
    
    dictFavourites = load_favourites()

    data = request.get_json()  # Parse the incoming JSON
    #user = data.get('user')
    if 'username' not in session:
        return jsonify({'success': True, 'message': 'Guest'})
    
    user = session["username"]
    cocktails = data.get('cocktails')
    print(cocktails)

    if not user:
        return jsonify({'success': False, 'error': 'Invalid data'}), 400
    

    # Save to favourites dictionary (or database)
    dictFavourites[session["username"]] = cocktails

    print(session["username"], cocktails)       

    with open(favourites_file, 'w') as file:
        yaml.dump(dictFavourites, file)

    return jsonify({'success': True, 'message': 'Favourites saved successfully'})



@app.route('/api/favourites/get', methods=['GET'])
def handle_favourites():
    if request.method == 'GET':
        # Check if the user is logged in

        if 'username' not in session:
            return jsonify({'success': True, "username": "Guest",  'error': 'User not logged in'})

        dictFavourites = load_favourites()  # Load existing favourites from YAML
        user = session['username']

        # Get the user's favourites or return an empty list if none exist
        user_favourites = dictFavourites.get(user, [])

        print({'success': True, 'username': user, 'favourites': user_favourites})
        return jsonify({'success': True, 'username': user, 'favourites': user_favourites})



if __name__ == '__main__':
    app.run(debug=True)


