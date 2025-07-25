from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.factory import Factory

import views.splash
import views.main
import views.head
import views.heada
import views.headb
import views.headc
import views.asthma
import views.asthmaa
import views.asthmab
import views.asthmac
import views.asthmad
import views.asthmae
import views.stomach
import views.stomacha
import views.stomachb
import views.stomachc
import views.stomachd
import views.stomache
import views.stomachf
import views.stomachg
import views.stomachh
import views.bone
import views.bonea
import views.boneb
import views.bonec
import views.boned
import views.bonee
import views.skin
import views.skina
import views.skinb
import views.skinc
import views.skind
import views.skine
import views.gland
import views.glanda
import views.glandb
import views.glandc
import views.glandd
import views.cancer
import views.cancera
import views.cancerb
import views.cancerc
import views.cancerd
import views.cancere
import views.cancerf
import views.kdiny
import views.kdinya
import views.kdinyb
import views.kdinyc
import views.kdinyd
import views.respa
import views.respaa
import views.respab
import views.respac
import views.respad
import views.respad
import views.respae
import views.respaf
import views.respag
import views.respah
import views.respai
import views.respaj
import views.respak
import views.respal
import views.eye
import views.eyea
import views.eyeb
import views.eyec
import views.baby
import views.babya
import views.babyb
import views.babyc
import views.babyd
import views.babye
import views.babyf
import views.babyg
import views.babyh
import views.babyi
import views.heart
import views.hearta
import views.heartb
import views.heartc
import views.heartd
import views.hearte
import views.heartf
import views.dev
import views.deva
import views.devb
import views.devc
import views.devd
import views.deve
import views.devf
import views.devg
import views.manu
import views.food
import views.fooda
import views.foodb
import views.foodc
import views.foode
import views.foodf
import views.tela
import views.telaa
import views.telab
import views.telac
import views.telad
import views.yaho
import views.yahoa
import views.yahob
import views.yahoc
import views.yahod
import views.game

class LazyScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen_classes = {
            'splash': ('kv/splash.kv', 'SplashScreen'),
            'main': ('kv/main.kv', 'MainScreen'),
            'head':('kv/head.kv', 'HeadScreen'),
            'heada':('kv/heada.kv', 'HeadaScreen'),
            'headb':('kv/headb.kv', 'HeadbScreen'),
            'headc':('kv/headc.kv', 'HeadcScreen'),
            'asthma':('kv/asthma.kv', 'AsthmaScreen'),
            'asthmaa':('kv/asthmaa.kv', 'AsthmaaScreen'),
            'asthmab':('kv/asthmab.kv', 'AsthmabScreen'),
            'asthmac':('kv/asthmac.kv', 'AsthmacScreen'),
            'asthmad':('kv/asthmad.kv', 'AsthmadScreen'),
            'asthmae':('kv/asthmae.kv', 'AsthmaeScreen'),
            'heart':('kv/heart.kv', 'HeartScreen'),
            'hearta':('kv/hearta.kv', 'HeartaScreen'),
            'heartb':('kv/heartb.kv', 'HeartbScreen'),
            'heartc':('kv/heartc.kv', 'HeartcScreen'),
            'heartd':('kv/heartd.kv', 'HeartdScreen'),
            'hearte':('kv/hearte.kv', 'HearteScreen'),
            'heartf':('kv/heartf.kv', 'HeartfScreen'), 
            'stomach':('kv/stomach.kv', 'StomachScreen'),
            'stomacha':('kv/stomacha.kv', 'StomachaScreen'),
            'stomachb':('kv/stomachb.kv', 'StomachbScreen'),
            'stomachc':('kv/stomachc.kv', 'StomachcScreen'),
            'stomachd':('kv/stomachd.kv', 'StomachdScreen'),
            'stomache':('kv/stomache.kv', 'StomacheScreen'),
            'stomachf':('kv/stomachf.kv', 'StomachfScreen'),
            'stomachg':('kv/stomachg.kv', 'StomachgScreen'),
            'stomachh':('kv/stomachh.kv', 'StomachhScreen'),
            'bone':('kv/bone.kv', 'BoneScreen'),
            'bonea':('kv/bonea.kv', 'BoneaScreen'),
            'boneb':('kv/boneb.kv', 'BonebScreen'),
            'bonec':('kv/bonec.kv', 'BonecScreen'),
            'boned':('kv/boned.kv', 'BonedScreen'),
            'bonee':('kv/bonee.kv', 'BoneeScreen'),
            'skin':('kv/skin.kv', 'SkinScreen'),
            'skina':('kv/skina.kv', 'SkinaScreen'),
            'skinb':('kv/skinb.kv', 'SkinbScreen'),
            'skinc':('kv/skinc.kv', 'SkincScreen'),
            'skind':('kv/skind.kv', 'SkindScreen'),
            'skine':('kv/skine.kv', 'SkineScreen'),
            'gland':('kv/gland.kv', 'GlandScreen'),
            'glanda':('kv/glanda.kv', 'GlandaScreen'),
            'glandb':('kv/glandb.kv', 'GlandbScreen'),
            'glandc':('kv/glandc.kv', 'GlandcScreen'),
            'glandd':('kv/glandd.kv', 'GlanddScreen'),
            'cancer':('kv/cancer.kv', 'CancerScreen'),
            'cancera':('kv/cancera.kv', 'CanceraScreen'),
            'cancerb':('kv/cancerb.kv', 'CancerbScreen'),
            'cancerc':('kv/cancerc.kv', 'CancercScreen'),
            'cancerd':('kv/cancerd.kv', 'CancerdScreen'),
            'cancere':('kv/cancere.kv', 'CancereScreen'),
            'cancerf':('kv/cancerf.kv', 'CancerfScreen'),
            'kdiny':('kv/kdiny.kv', 'KdinyScreen'),
            'kdinya':('kv/kdinya.kv', 'KdinyaScreen'),
            'kdinyb':('kv/kdinyb.kv', 'KdinybScreen'),
            'kdinyc':('kv/kdinyc.kv', 'KdinycScreen'),
            'kdinyd':('kv/kdinyd.kv', 'KdinydScreen'),
            'respa':('kv/respa.kv', 'RespaScreen'),
            'respaa':('kv/respaa.kv', 'RespaaScreen'),
            'respab':('kv/respab.kv', 'RespabScreen'),
            'respac':('kv/respac.kv', 'RespacScreen'),
            'respad':('kv/respad.kv', 'RespadScreen'),
            'respae':('kv/respae.kv', 'RespaeScreen'),
            'respaf':('kv/respaf.kv', 'RespafScreen'),
            'respag':('kv/respag.kv', 'RespagScreen'),
            'respah':('kv/respah.kv', 'RespahScreen'),
            'respai':('kv/respai.kv', 'RespaiScreen'),
            'respaj':('kv/respaj.kv', 'RespajScreen'),
            'respak':('kv/respak.kv', 'RespakScreen'),
            'respal':('kv/respal.kv', 'RespalScreen'),
            'eye':('kv/eye.kv', 'EyeScreen'),
            'eyea':('kv/eyea.kv', 'EyeaScreen'),
            'eyeb':('kv/eyeb.kv', 'EyebScreen'),
            'eyec':('kv/eyec.kv', 'EyecScreen'),
            'baby':('kv/baby.kv', 'BabyScreen'),
            'babya':('kv/babya.kv', 'BabyaScreen'),
            'babyb':('kv/babyb.kv', 'BabybScreen'),
            'babyc':('kv/babyc.kv', 'BabycScreen'),
            'babyd':('kv/babyd.kv', 'BabydScreen'),
            'babye':('kv/babye.kv', 'BabyeScreen'),
            'babyf':('kv/babyf.kv', 'BabyfScreen'),
            'babyg':('kv/babyg.kv', 'BabygScreen'),
            'babyh':('kv/babyh.kv', 'BabyhScreen'),
            'babyi':('kv/babyi.kv', 'BabyiScreen'),
            'dev':('kv/dev.kv', 'DevScreen'),
            'deva':('kv/deva.kv', 'DevaScreen'),
            'devb':('kv/devb.kv', 'DevbScreen'),
            'devc':('kv/devc.kv', 'DevcScreen'),
            'devd':('kv/devd.kv', 'DevdScreen'),
            'deve':('kv/deve.kv', 'DeveScreen'),
            'devf':('kv/devf.kv', 'DevfScreen'),
            'devg':('kv/devg.kv', 'DevgScreen'),
            'manu':('kv/manu.kv', 'ManuScreen'),
            'food':('kv/food.kv', 'FoodScreen'),
            'fooda':('kv/fooda.kv', 'FoodaScreen'),
            'foodb':('kv/foodb.kv', 'FoodbScreen'),
            'foodc':('kv/foodc.kv', 'FoodcScreen'),
            'foode':('kv/foode.kv', 'FoodeScreen'),
            'foodf':('kv/foodf.kv', 'FoodfScreen'),
            'tela':('kv/tela.kv', 'TelaScreen'),
            'telaa':('kv/telaa.kv', 'TelaaScreen'),
            'telba':('kv/telaa.kv', 'TelaaScreen'),
            'telab':('kv/telab.kv', 'TelabScreen'),
            'telac':('kv/telac.kv', 'TelacScreen'),
            'telad':('kv/telad.kv', 'TeladScreen'),
            'yaho':('kv/yaho.kv', 'YahoScreen'),
            'yahoa':('kv/yahoa.kv', 'YahoaScreen'),
            'yahob':('kv/yahob.kv', 'YahobScreen'),
            'yahoc':('kv/yahoc.kv', 'YahocScreen'),
            'yahod':('kv/yahod.kv', 'YahodScreen'),
            'game':('kv/game.kv', 'GameScreen'),


        }
    def switch_to_screen(self, screen_name):
        if not self.has_screen(screen_name):
            kv_file, class_name = self.screen_classes[screen_name]
            Builder.load_file(kv_file)
            screen_class = Factory.get(class_name)
            screen_instance = screen_class(name=screen_name)
            self.add_widget(screen_instance)
        self.current = screen_name
