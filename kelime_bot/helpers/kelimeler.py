import random
kelimeler = ["gözəl ","biliksiz ","xətalı","sağalmaq","buraxmaq","zaman","su","etmək","istifadə","dəyər","görmək", 
              "yenidən", "çoxlu", "fəqət", "manat", "oynamaq", "çiçək", "şəhər", "yüksəlmək", "mübarizə", "varlıq", "yemək", 
              "güvən", "gərək", "şəfa", "birlik", "rahat", "soyuq", "vətən", "kitab", "paylaşmaq", "hesab", "bədən", 
              "torpaq", "eynək", "sistem", "xoş", "çəkilmək", "tekniki", "yaxınlaşmaq", "rayon", "tarix", "sevgi", "bacı", 
              "incə", "mayor", "qoyun", "qarşılıqlı","vermək", "sahib", "artıq", "kişi", "digər", "qadın", "yenə", "aşbaz", 
              "dəftər", "hadisə", "öpməl", "siz", "dövlət", "qabağ", "manyak", "baxmaq", "üzərində", "bölgə", "bəzi", "başlamaq", 
              "tutmaa", "birbir", "heçbir", "gəlmək", "şaftalı", "usta", "hal", "doğru", "orta", "başqa", "böyük", "etməmək", 
              "almaq", "üzmək", "sual", "həsrət", "çəkmək", "siqaret", "kömək", "səs", "anlamaq", "toyuq", "saat", "dünya", 
              'birlikdə', 'sevmək', 'qalmaq', 'yarpaq', 'ağac', 'yer', 'cütlük', 'demək', 'çox', 'uçmaq', 'alçaq', 'bənzər', 'daha', 'alma', 
              'vəfasız', 'xüsusi', 'darıxmaq', 'pambıq', 'vermək', 'amma', 'sonra', 'kədər', 'imtahan', 'məhsul', 'insan', 'şəkər', 'sağlıq', 
              'istəmək', 'üzsüz', 'xəncər', 'cəngavər', 'sıyırmaq', 'kariyera', 'qüsul', 'biznes', 'pendir', 'aralıq', 'şərəf', 'bilmək', 'orqan', 'zaman', 
              'dadsız', 'hasar', 'dam', 'rəşid', 'travmotologiya', 'tük', 'dəvə', 'yox', 'oba', 'həssas', 'döşəkçə', 'qara', 'qoz', 
              'stansiya', 'traxtor', 'ixtişaş', 'cins', 'səma', 'mavi', 'diyar', 'təpə', 'uşaqlar', 'əbədi', 'ədəb', 
              'baş', 'dayanacaq', 'ötüşmək', 'ötmək', 'rəqəmsal', 'min', 'yeni', 'kart', 'yaşma', 'əhval', 'orta', 'lider', 'yurd', 'paytaxt', 
              'yemək', 'boşluq', 'həyasız', 'abır', 'nəsil', 'qarışqa', 'tapmaq', 'səhnə', 'yaşamaq', 'təsəvvür', 'eyni', 'daxili', 'xarici', 
              'kişi', 'murdar', 'mübdəta', 'ilk', 'bacarıqsız', 'ön', 'son', 'rahatlıq', 'şəkil', 'video', 'tanınmaq', 'həmçinin', 'ağlamaü', 'gülməmək', 
              'alt', 'gətirmək', 'pərdə', 'vərəq', 'tərəf', 'azarkeş', 'adam', 'kamanda', 'tənha', 'batırmaq', 'stol', 'səslənmək', 'kömək', 
              'doğru', 'dayanmaq', 'qız', 'bütün', 'tüstü', 'povest', 'mənlik', 'çətinlik', 'ana', 'astar', 'bəzi', 'baba', 'google', 
              'sadəcə', 'balaca', 'böyük', 'pozğun', 'ərəb', 'nektar', 'gündüz', 'riyaziyyat', 'sevda', 'sağalmaq', 'nəticə', 'yapışdırıcı', 'super', 
              'soyad', 'ferma', 'qədər', 'reanimasiya', 'açmaq', 'tibb', 'təcili', 'yanğım', 'yaşıllıq', 'saat', 'yaş', 'doğru', 'sirr', 
              'sahib', 'sıra', 'yarımçıq', 'batarya', 'aylıq', 'abone', 'tutmaq', 'atmaü', 'əvəzlik', 'yorulmaq', 'eşitmək', 'söz', 'başlıq', 
              'sevmək', 'biraz', 'çətin', 'soyunmaq', 'ölçmək', 'döyülmək', 'tek', 'üstün', 'kopyalamaq', 'öyrəşmək', 'vüsal', 'danışmaq', 'saxsı', 
              'kor', 'şərəf', 'bölük', 'komutan', 'gecəyarı', 'ekran', 'namus', 'işsiz', 'gözləmək', 'uzun', 'klinika', 'bugün', 'kosa', 
              'dostlar', 'düzəltmək', 'ailə', 'qəpik', 'əzbər', 'oğlan', 'hərkəs', 'qüvvət', 'bəlkə', 'babnik', 'tam', 'qayğılı', 'münasibət', 
              'fiqur', 'köhnə', 'axtarmaq', 'yay', 'əzbərləmək', 'yaxın', 'dalan', 'bəy', 'xoruz', 'hörmətsiz', 'bölmək', 'özəl', 'ağıllı', 
              'dul', 'pomidor', 'məsləhət', 'gərəkli', 'türkiyə', 'mənasız', 'asfalt', 'quş', 'taleh', 'ayaq', 'daşımaq', 'geri', 'buğda', 
              'iynə', 'məmulat', 'növ', 'qanunsuz', 'zalım', 'hava', 'sayı', 'fərqli', 'qrup', 'taxta', 'hektar', 'qovuşmaq', 'bibi', 
              'allah', 'leysan', 'poçt', 'qədəh', 'ilk', 'uğur', 'qazanmaq', 'payız', 'litsey', 'açıq', 'öyrətmək', 'sürmək', 'dil', 'şirkət', 'qaynaq', 'bitmək', 'sorğu', 'dayanmaq', 'sağ', 'rəng', 'xoş', 'haqq', 'inanmaq', 
              'çalışmaq', 'bibər', 'parça', 'kafe', 'ingilis', 'ayaqqabı', 'dəyər', 'məhşur', 'faiz', 'doktor', 'gəlir', 
              'tapşırıq', 'layihə', 'bölgə', 'film', 'dəniz', 'müştəri', 'otel', 'telefon', 'dayı', 'okean', 'ikinci', 
              'qalxmaq', 'xətt', 'paltar', 'üzeyir', 'elçi', 'bağırsaq', 'düşüncə', 'milyon', 'çexol', 'dondurma', 'bünövrə', 
              'yaratmaq', 'hərbi', 'hissə', 'keçirmək', 'ənənə', 'konsert', 'gizir', 'avro', 'rəsim', 'işıq', 'atçılıq', 
              'xanım', 'xidmət', 'ehtiyac', 'nöqtə', 'dağ', 'təsdiq', 'oyun', 'fakt', 'yenidən', 'işlək', 'qısa', 'kimya', 
              'bank', 'müddət', 'əsil', 'qəbul', 'məftun', 'diqqətsiz', 'uzaq', 'kompyuter', 'oturmaq', 'qazlı', 
              'bəylik', 'oğul', 'dinləmək', 'uyğun', 'dollar', 'istehsal', 'dəqiqə', 'unutmaq', 'yerimək', 'beləcə', 'pis', 
              'divar', 'ağız', 'duyğu', 'əməl', 'itki', 'mömin', 'xeyli', 'zəlil', 'şikəst', 'mümkün', 'soydaş', 
              'ulduz', 'beş', 'sənət', 'ana', 'xəstəlik', 'şagird', 'çiyələk', 'çəlik', 'masa', 'ölmək', 'komando', 'üst', 
              'zadəgan', 'musiqi', 'ayrılmaq', 'enerji', 'universitet', 'sport', 'fitnes', 'can', 'rəğmən', 'qüsur', 'ölüm', 
              'davamlı', 'sağlıq', 'ukrayna', 'xəcalət', 'hiss', 'bal', 'sabah', 'internet', 'saz', 'çöl', 
              'mərkəz', 'ortam', 'yerində', 'cənub', 'kənd', 'quldarlıq', 'aşağı', 'mal', 'inanmaq', 'budaq', 'prospekt', 'axşam', 
              'araştırmaq', 'götürmək', 'qatılmaq', 'yoxsul', 'qurutmaq', 'bilmək', 'fərz', 'qan', 'xəstə', 'səhər', 'düşmək', 
              'salfet', 'bilikli', 'həftə', 'yoldaş', 'hesab', 'avtomobil', 'əcnəbi', 'davranış', 'otaq', 'winston', 'bəzənmək', 
              'bəlli', 'ayrı', 'qiymət', 'haqqında', 'qaldırmaq', 'qol', 'yalnız', 'qapı', 'şüşə', 'sonunda', 'yavaş', 
              'sənədsiz', 'önəmli', 'oyun', 'yalnış', 'varlıq', 'səviyyə', 'qayğı', 'inək', 'satış', 'içəri', 'adət', 'sahiblənmək', 
              'ekonomiya', 'acı', 'xeyr', 'qorumaq', 'qatıq', 'ifadə', 'asmaq', 'tapmaq', 'fotoqraf', 'heyvan', 'döyüş', 
              'mal', 'saç', 'itirmək', 'geri', 'yerləşdirmək', 'dörd', 'gerçək', 'səhifə', 'texnologiya', 'məşğul', 'beş', 
              'sektor', 'geniş', 'kağız', 'qoxu', 'sağ', 'içki', 'möhtəşəm', 'küçə', 'makler', 'sürmək', 'istifadə', 'sinf', 
              'plov', 'doğmaq', 'ağır', 'təkrar', 'günəş', 'vodka', 'gülüş', 'söz', 'bina', 'həyat', 'oynamaq', 'mübarək', 'yataü', 
              'yazar', 'qulaq', 'müəllimə', 'səbəb', 'ayıq', 'bəli', 'yağ', 'yüz', 'anlatmaq', 'başsız', 'gülmək', 'məcəllə', 
              'satmaq', 'anqut', 'göndərmək', 'medal', 'firma', 'hökumət', 'qəlb', 'robot', 'proses', 'şəbəkə', 'stul', 'künc', 
              'vurğu', 'model', 'balıq', 'bazar', 'görüş', 'yarasa', 'hazırlanmaq', 'miqdar', 'birinci', 'meydan', 'ölçü', 
              'seçmək', 'stiker', 'baxça', 'ibrət', 'çörək', 'bəstəboy', 'manikür', 'dolu', 'qurum', 'saysız', 'qorxmaq', 
              'yardım', 'qonaqpərvər', 'ədviyyat', 'xoşlanmaq', 'pişik', 'populyar', 'böyütmək', 'dolaşmaq', 'maddə', 'üstələmək', 
              'yaşlanmaq', 'sarışın', 'istək', 'yanaşmaq', 'deşmək', 'xala', 'dil', 'ədat', 'çalmaq', 'icazə', 'qorxu', 
              'ixtisas', 'polis', 'yalnızlıq', 'açıqlamaq', 'fikr', 'səssizcə', 'pəncərə', 'qazan', 'daş', 'atəş', 'lovğa', 
              'yeniyetmə', 'era', 'vəsiqə', 'qayda', 'məhəllə', 'mətbəx', 'dənə', 'istehlak', 'üstünə', 'dayanmaq', 'incə', 
              'qaç', 'ortalama', 'tip', 'görüntü', 'bəhr', 'dərs', 'azzar', 'növbəti', 'xilas', 'nömrə', 'döymək', 'anlayış', 'əriştə', 'basmaq', 'soxmaq', 'kontrol', 'çevirmək', 'din', 'güclü', 'hələlik', 'plan', 'beyin', 
              'elektrik', 'qadın', 'üzmək', 'park', 'sallanmaq', 'deyinmək', 'film', 'uçmaq', 'partiya', 'iynə', 'ruh', 
              'sevgili', 'yaxınlaşmaq', 'müddət', 'baxış', 'bilikli', 'ilham', 'sima', 'göy', 'xatırlamaq', 'qəza', 
              'yaxşı', 'dağ', 'bağlamaq', 'addım', 'ciddi', 'çarə', 'sevilmək', 'bələdiyyə', 'internet', 'seçim', 
              'ağlamaq', 'kino', 'davranış', 'yollamaq', 'fəaliyət', 'zərər', 'dərin', 'salon', 'növ', 'kəsilmək', 
              'İzləmək', 'anidən', 'söyləmək', 'seçilmiş', 'vurma', 'acmaq', 'bağırmaq', 'öskürmək', 'davranmaq', 
              'məktup', 'soyuqqanlı', 'canlı', 'klavyatura', 'maşın', 'yararlanmaq', 'cavan', 'boş', 'gözəllik', 'futboll', 'inzibatçı', 
              'metr', 'polis', 'tutulmaq', 'keyfiyyət', 'bitki', 'dəyişiklik', 'dərman', 'kredit', 'ölmək', 'faydalanmaq', 
              'rəsmi', 'imkan', 'cəza', 'murad', 'incələmək', 'top', 'profesional', 'doldurmaq', 'kanal', 'yaddaş', 'durmaq', 
              'illik', 'məktəb', 'iqlim', 'mühit', 'barmaq', 'zarafat', 'yollanmaq', 'soyuqluq', 'normal', 'istilənmək', 
              'kələm', 'qırmızı', 'rol', 'oyanmaq', 'fəhlə', 'gəlin', 'bənzəmək', 'yalançı', 'müəllim', 'boy', 'günlük', 'politika', 
              'suç', 'niye', 'sahne', 'sokmak', 'adet', 'koltuk', 'kurtarmak', 'sanatçı', 'tercihetmek', 'uzanmak', 'aşama', 
              'Əlavə', 'meşə', 'ayırmaq', 'düzmək', 'faiz', 'gəlinlik', 'indiki', 'hekayə', 'hüceyrə', 'nəzik', 'roman', 
              'vergi', 'yaxmaq', 'qardaş', 'jurnal', 'dəstək', 'geyinmək', 'xəta', 'hədd', 'birlik', 'ilan', 'qarşılamaq', 
              'yarı', 'qaçmaq', 'gündüz', 'qaranlıq', 'avtobus', 'sənaye', 'uşaq', 'vətəndaş', 'nazir', 'kürə', 'millət', 
              'reklam', 'yüksək', 'köynək', 'qəzet', 'infeksiya', 'sosial', 'birləşmək', 'keçmiş', 'xəstəxana', 'oxşamaq', 
              'iclas', 'müxbir', 'içmək', 'inanc', 'şalvar', 'sayğac', 'bitirmək', 'real', 'giriş', 'rahat', 
              'toplam', 'bərabər', 'dükkan', 'gizli', 'benzer', 'dəri', 'döndərmək', 'öhdəlik', 'problem', 'servis', 'müalicə', 
              'yaşıl', 'prezident', 'basqın', 'çıxçölə', 'cümlə', 'diləmək', 'azadlıq', 'nəsimi', 'şəxsiyyət', 'vəziyyət', 'üçüncü', 
              'aktual', 'dəyərləndirmək', 'qəribə', 'sürücü', 'süd', 'tutmaq', 'əşya', 'ölkələrarası', 'üzv', 
              'ağırlıq', 'milyard', 'çənə', 'sıxıntı', 'allah', 'trip', 'toplama', 'yayım', 'diqqətli', 'dərəcə', 
              'oxumaq', 'yatmaq', 'yavaş', 'qarışmaq', 'tehlükə', 'vaxt', 'dairə', 'fürsət', 'işləmək', 'qarışdırmaq', 
              'qatqı', 'şeir', 'tamam', 'təyyarə', 'cavab', 'təbiət', 'evlənmək', 'burun', 'pul', 'əlbəttə', 'işçi', 'işletmək', 
              'qısaca', 'mağaza', 'mediya', 'yüzünden', 'artım', 'kəsdirmək', 'koma', 'sığorta', 'yazmaq', 'ürək', 'sənəd', 
              'qıç', 'namazova', 'ifadə', 'risk', 'qeybət', 'söndürmək', 'demokratiya', 'duzlamaq', 'mədrəsə', 'dövr', 'düşük', 
              'etiraf', 'sürətli', 'festival', 'ümumi', 'öldürmək', 'gələcək', 'xatirə', 'pozmaq', 'maraqlanmaq', 'meyvə', 'takılmak', 
              'şirin', 'baldır', 'dəyişmək', 'qanun', 'külək', 'təşkilat', 'dodağ', 'tərz', 'yeddi', 'azalmaq', 
              'bağlamaq', 'televizor', 'dialoq', 'müdür', 'otel', 'xəbər', 'zövq', 'minmək', 'maşın', 'hüquq', 
              'namaz', 'modern', 'şöhrət', 'silah', 'tələb', 'ulduz', 'yoğun', 'əsgər', 'asand', 'ördək', 'qaz', 
              'proqram', 'doğulmaq', 'bəyannamə', 'besin', 'dünən', 'görüşmək', 'yaşlı', 'alışveriş', 'qüdrət', 'çərçivə', 
              'lazım', 'mövcud', 'xala', 'uzadmaq', 'yönləndirmək', 'eşşək', 'bağlanmaq', 'məsəl', 'eşq', 'sayt', 
              'ana', 'ata', 'maxe', 'kimsəsiz', 'hörmət', 'ödəmək', 'istedad', 'kilo', 'paylaşmaq', 'sərt', 'ağıl',
              'şair', 'şimal', 'fərq', 'dəbilqə', 'teatr', 'dəyişik', 'hədəf', 'povest', 'dost', 'alov', 'anlayış', 'əriştə', 'basmaq', 'soxmaq', 'kontrol', 'çevirmək', 'din', 'güclü', 'hələlik', 'plan', 'beyin', 
              'elektrik', 'qadın', 'üzmək', 'park', 'sallanmaq', 'deyinmək', 'film', 'uçmaq', 'partiya', 'iynə', 'ruh', 
              'sevgili', 'yaxınlaşmaq', 'müddət', 'baxış', 'bilikli', 'ilham', 'sima', 'göy', 'xatırlamaq', 'qəza', 
              'yaxşı', 'dağ', 'bağlamaq', 'addım', 'ciddi', 'çarə', 'sevilmək', 'bələdiyyə', 'internet', 'seçim', 
              'ağlamaq', 'kino', 'davranış', 'yollamaq', 'fəaliyət', 'zərər', 'dərin', 'salon', 'növ', 'kəsilmək', 
              'İzləmək', 'anidən', 'söyləmək', 'seçilmiş', 'vurma', 'acmaq', 'bağırmaq', 'öskürmək', 'davranmaq', 
              'məktup', 'soyuqqanlı', 'canlı', 'klavyatura', 'maşın', 'yararlanmaq', 'cavan', 'boş', 'gözəllik', 'futboll', 'inzibatçı', 
              'metr', 'polis', 'tutulmaq', 'keyfiyyət', 'bitki', 'dəyişiklik', 'dərman', 'kredit', 'ölmək', 'faydalanmaq', 
              'rəsmi', 'imkan', 'cəza', 'murad', 'incələmək', 'top', 'profesional', 'doldurmaq', 'kanal', 'yaddaş', 'durmaq', 
              'illik', 'məktəb', 'iqlim', 'mühit', 'barmaq', 'zarafat', 'yollanmaq', 'soyuqluq', 'normal', 'istilənmək', 
              'kələm', 'qırmızı', 'rol', 'oyanmaq', 'fəhlə', 'gəlin', 'bənzəmək', 'yalançı', 'müəllim', 'boy', 'günlük', 'politika', 
              'suç', 'niye', 'sahne', 'sokmak', 'adet', 'koltuk', 'kurtarmak', 'sanatçı', 'tercihetmek', 'uzanmak', 'aşama', 
              'Əlavə', 'meşə', 'ayırmaq', 'düzmək', 'faiz', 'gəlinlik', 'indiki', 'hekayə', 'hüceyrə', 'nəzik', 'roman', 
              'vergi', 'yaxmaq', 'qardaş', 'jurnal', 'dəstək', 'geyinmək', 'xəta', 'hədd', 'birlik', 'ilan', 'qarşılamaq', 
              'yarı', 'qaçmaq', 'gündüz', 'qaranlıq', 'avtobus', 'sənaye', 'uşaq', 'vətəndaş', 'nazir', 'kürə', 'millət', 
              'reklam', 'yüksək', 'köynək', 'qəzet', 'infeksiya', 'sosial', 'birləşmək', 'keçmiş', 'xəstəxana', 'oxşamaq', 
              'iclas', 'müxbir', 'içmək', 'inanc', 'şalvar', 'sayğac', 'bitirmək', 'real', 'giriş', 'rahat', 
              'toplam', 'bərabər', 'dükkan', 'gizli', 'benzer', 'dəri', 'döndərmək', 'öhdəlik', 'problem', 'servis', 'müalicə', 
              'yaşıl', 'prezident', 'basqın', 'çıxçölə', 'cümlə', 'diləmək', 'azadlıq', 'nəsimi', 'şəxsiyyət', 'vəziyyət', 'üçüncü', 
              'aktual', 'dəyərləndirmək', 'qəribə', 'sürücü', 'süd', 'tutmaq', 'əşya', 'ölkələrarası', 'üzv', 
              'ağırlıq', 'milyard', 'çənə', 'sıxıntı', 'allah', 'trip', 'toplama', 'yayım', 'diqqətli', 'dərəcə', 
              'oxumaq', 'yatmaq', 'yavaş', 'qarışmaq', 'tehlükə', 'vaxt', 'dairə', 'fürsət', 'işləmək', 'qarışdırmaq', 
              'qatqı', 'şeir', 'tamam', 'təyyarə', 'cavab', 'təbiət', 'evlənmək', 'burun', 'pul', 'əlbəttə', 'işçi', 'işletmək', 
              'qısaca', 'mağaza', 'mediya', 'yüzünden', 'artım', 'kəsdirmək', 'koma', 'sığorta', 'yazmaq', 'ürək', 'sənəd', 
              'qıç', 'namazova', 'ifadə', 'risk', 'qeybət', 'söndürmək', 'demokratiya', 'duzlamaq', 'mədrəsə', 'dövr', 'düşük', 
              'etiraf', 'sürətli', 'festival', 'ümumi', 'öldürmək', 'gələcək', 'xatirə', 'pozmaq', 'maraqlanmaq', 'meyvə', 'takılmak', 
              'şirin', 'baldır', 'dəyişmək', 'qanun', 'külək', 'təşkilat', 'dodağ', 'tərz', 'yeddi', 'azalmaq', 
              'bağlamaq', 'televizor', 'dialoq', 'müdür', 'otel', 'xəbər', 'zövq', 'minmək', 'maşın', 'hüquq', 
              'namaz', 'modern', 'şöhrət', 'silah', 'tələb', 'ulduz', 'yoğun', 'əsgər', 'asand', 'ördək', 'qaz', 
              'proqram', 'doğulmaq', 'bəyannamə', 'besin', 'dünən', 'görüşmək', 'yaşlı', 'alışveriş', 'qüdrət', 'çərçivə', 
              'lazım', 'mövcud', 'xala', 'uzadmaq', 'yönləndirmək', 'eşşək', 'bağlanmaq', 'məsəl', 'eşq', 'sayt', 
              'ana', 'ata', 'maxe', 'kimsəsiz', 'hörmət', 'ödəmək', 'istedad', 'kilo', 'paylaşmaq', 'sərt', 'ağıl', 'çay', 'gölməçə', 'dəniz', 'zəngin', 'əsla', 'sözlər', 'islanmaq', 'aşiq', 'yaşamaq', 'boyun', 'mobil', 
              'həndəsə', 'baba', 'bel', 'dolayı', 'qəhvə', 'əzələ', 'məclis', 'əvvəl', 'əziyyət', 'ünvan', 'polkovnik', 
              'paşa', 'istilik', 'tamam', 'inam', 'ticarət', 'market', 'yararlı', 'yaymaq', 'axmaq', 'çimmək', 'düşünülmək', 
              'könül', 'xəyal', 'irəliləmək', 'şərab', 'yuxarı', 'qızıl', 'alqı', 'satqı', 'səssiz', 'təmiz', 
              'vitamin', 'sürət', 'keç', 'hərəkət', 'yumurta', 'yüksək', 'ahuzar', 'dilək', 'kəsmik', 'sinir', 'birgəlik', 
              'qapanmaq' 
              ]

def kelime_sec():
    return random.choice(kelimeler)
