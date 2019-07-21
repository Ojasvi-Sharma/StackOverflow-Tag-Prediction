from flask import Flask, jsonify, request
import numpy as np
from sklearn.externals import joblib
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.externals import joblib
from bs4 import BeautifulSoup
import re
from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem.snowball import SnowballStemmer
from nltk.tokenize import word_tokenize
import nltk
import cloudpickle
import joblib
from flask_cors import CORS

import flask
app = Flask(__name__)

CORS(app)

nltk.download('punkt') 

tag_list = ['c#', 'java', 'php', 'javascript', 'android', 'jquery', 'c++',
       'python', 'iphone', 'asp.net', 'mysql', 'html', '.net', 'ios',
       'sql', 'css', 'objective-c', 'linux', 'ruby-on-rails', 'windows',
       'c', 'sql-server', 'ruby', 'xml', 'wpf', 'ajax', 'database',
       'regex', 'asp.net-mvc', 'windows-7', 'osx', 'django', 'xcode',
       'arrays', 'vb.net', 'eclipse', 'ruby-on-rails-3', 'facebook',
       'ubuntu', 'json', 'performance', 'networking', 'multithreading',
       'string', 'winforms', 'security', 'visual-studio-2010',
       'asp.net-mvc-3', 'bash', 'homework', 'image', 'html5', 'wcf',
       'wordpress', 'algorithm', 'forms', 'web-services', 'perl',
       'visual-studio', 'sql-server-2008', 'query', 'oracle', 'git',
       'linq', 'flash', 'actionscript-3', 'apache2', 'email', 'apache',
       'spring', 'cocoa', 'r', 'silverlight', 'ipad', 'swing',
       'cocoa-touch', 'hibernate', 'excel', 'entity-framework', 'file',
       'flex', 'list', 'api', 'internet-explorer', 'firefox', '.htaccess',
       'shell', 'delphi', 'google-chrome', 'sqlite', 'qt', 'jquery-ui',
       'tsql', 'unix', 'svn', 'node.js', 'http', 'windows-xp',
       'debugging', 'oop', 'unit-testing', 'postgresql', 'class',
       'codeigniter', 'google-app-engine', 'iis', 'sql-server-2005',
       'function', 'sockets', 'matlab', 'templates', 'windows-phone-7',
       'memory', 'ssh', 'command-line', 'search', 'validation', 'parsing',
       'google-maps', 'windows-server-2008', 'jsp', 'pdf', 'mongodb',
       'winapi', 'dns', 'authentication', 'zend-framework', 'calculus',
       'xaml', 'scala', 'mvc', 'plugins', 'vim', 'nhibernate',
       'linear-algebra', 'uitableview', 'events', 'sharepoint', 'vba',
       'visual-studio-2008', 'audio', 'design', 'rest', 'optimization',
       'url', 'video', 'magento', 'tomcat', 'c#-4.0', 'real-analysis',
       'jsf', 'session', 'google', 'jquery-ajax', 'android-layout',
       'design-patterns', 'variables', 'java-ee', 'logging', 'css3',
       'exception', 'facebook-graph-api', 'generics', 'date', 'caching',
       'table', 'testing', 'listview', 'math', 'cakephp', 'mod-rewrite',
       'redirect', 'ssl', 'drupal', 'gui', 'gwt', 'probability',
       'powershell', 'sorting', 'centos', 'datetime', 'ms-access',
       'permissions', 'dom', 'maven', 'xslt', 'debian', 'visual-c++',
       'web-applications', 'mac', 'ios5', 'database-design', 'encryption',
       'inheritance', 'loops', 'object', 'phonegap', 'active-directory',
       'haskell', 'nginx', 'animation', 'opengl', 'pointers', 'core-data',
       'grails', 'browser', 'jquery-mobile', 'linq-to-sql', 'servlets',
       'windows-server-2003', 'deployment', 'layout', 'graphics',
       'backup', 'iis7', 'mobile', 'configuration', 'abstract-algebra',
       'fonts', 'gcc', 'activerecord', 'post', 'windows-8', 'select',
       'button', 'application', 'emacs', 'div', 'data-binding',
       'geometry', 'image-processing', 'memory-management', 'dynamic',
       'jpa', 'architecture', 'asp.net-mvc-2', 'opencv', 'gridview',
       'netbeans', 'version-control', 'text', 'iframe', 'serialization',
       'jquery-plugins', 'extjs', 'login', 'spring-mvc', 'cookies',
       'installation', 'scripting', 'combinatorics', 'dll', 'printing',
       'file-upload', 'boost', 'soap', 'join', 'user-interface',
       'amazon-ec2', 'stored-procedures', 'hard-drive', 'blackberry',
       'encoding', 'ftp', 'script', 'mvvm', 'reflection', 'service',
       'statistics', 'xpath', 'proxy', 'filesystems', 'assembly',
       'macros', 'unicode', 'usb', 'csv', 'iphone-sdk-4.0', 'curl',
       'javascript-events', 'razor', 'data-structures',
       'general-topology', 'data', 'google-maps-api-3', 'twitter',
       'process', 'collections', 'asynchronous', 'sequences-and-series',
       'windows-vista', 'azure', 'jdbc', 'terminal', 'android-intent',
       'canvas', 'tcp', 'time', 'wireless-networking', 'batch',
       'excel-vba', 'analysis', 'binding', 'file-io', 'random', 'orm',
       'backbone.js', 'reporting-services', 'actionscript', 'syntax',
       'graph', 'algebra-precalculus', 'joomla', 'webserver', 'web',
       'ant', 'keyboard', 'windows-server-2008-r2', 'routing', 'https',
       'heroku', 'recursion', 'symfony2', 'methods', 'selenium',
       'if-statement', 'view', 'dictionary', 'uitableviewcell',
       'drop-down-menu', 'group-theory', 'number-theory',
       'entity-framework-4', 'uiview', 'concurrency', 'matrices',
       'properties', 'types', 'exception-handling', 'language-agnostic',
       'opengl-es', 'compiler', 'complex-analysis', 'url-rewriting',
       'vpn', '.net-4.0', 'open-source', 'com', 'boot', 'virtualbox',
       'website', 'hash', 'cron', 'input', 'tikz-pgf', 'vector',
       'asp.net-mvc-4', 'sharepoint2010', '2010', 'interface',
       'localization', 'twitter-bootstrap', 'asp-classic', 'java-me',
       'coldfusion', 'utf-8', 'formatting', 'mercurial', 'virtualization',
       'batch-file', 'ip', 'amazon-web-services', 'map', 'colors',
       'router', 'groovy', 'frameworks', 'stl', 'autocomplete',
       'memory-leaks', 'import', 'silverlight-4.0', 'delete',
       'django-models', 'programming-languages', 'xcode4',
       'character-encoding', 'for-loop', '3d', 'oauth', 'parameters',
       'logic', 'path', 'usercontrols', 'firewall', 'datagrid', 'jboss',
       'jqgrid', 'keyboard-shortcuts', 'coding-style', 'model',
       'reference', 'build', 'functional-analysis', 'internet-explorer-8',
       'microsoft-excel', 'reference-request', 'jsf-2', 'error-handling',
       'github', 'multidimensional-array', 'menu', 'sdk',
       'jquery-selectors', 'functions', 'outlook', 'safari', 'vbscript',
       'filter', 'smtp', 'background', 'static', 'sed', 'datagridview',
       'solr', 'upload', 'air', 'graph-theory', 'hadoop', 'python-2.7',
       'automation', 'documentation', 'activity', 'dependency-injection',
       'junit', 'laptop', 'mfc', 'tabs', 'internationalization',
       'internet', 'jar', 'uiwebview', 'tfs', 'uiviewcontroller',
       'youtube', 'ide', 'c++11', 'charts', 'combobox', 'maven-2',
       'checkbox', 'casting', 'clojure', 'exchange', 'numpy', 'rss',
       'android-emulator', 'licensing', 'matrix', 'struts2', 'console',
       'integral', 'navigation', 'vb6', 'calendar', 'amazon-s3',
       'connection', 'module', 'crash', 'passwords', 'tags', 'migration',
       'ruby-on-rails-3.1', 'constructor', 'triggers', 'textbox', 'awk',
       'ado.net', 'download', 'elementary-number-theory', 'resources',
       '.net-3.5', 'msbuild', 'osx-lion', 'hyperlink', 'monitoring',
       'uinavigationcontroller', 'dojo', 'workflow', 'mono', 'io', 'ssis',
       'algebraic-geometry', 'attributes', 'custom-post-types',
       'windows-services', 'xhtml', 'dialog', 'drag-and-drop', 'ios6']

tag_list = np.array(tag_list)

def decontracted(phrase):
    # specific
    phrase = re.sub(r"won't", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase


stop_words= set(['br', 'the', 'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've",\
            "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', \
            'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their',\
            'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', \
            'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', \
            'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', \
            'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after',\
            'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further',\
            'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more',\
            'most', 'other', 'some', 'such', 'only', 'own', 'same', 'so', 'than', 'too', 'very', \
            's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', \
            've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn',\
            "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn',\
            "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", \
            'won', "won't", 'wouldn', "wouldn't"])

clf = joblib.load('lr_with_more_title_weight.pkl')
count_vect = joblib.load('count_vect.pkl')

#vectorizer = cloudpickle.load(open('vect.pkl','rb'))
#clf = joblib.load("lr_with_more_title_weight.pkl")

def striphtml(data):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, ' ', str(data))
    return cleantext
def stripcode(data):
    # flags= re.DOTALL matches \n also
    return re.sub('<code>(.*?)</code>', '', str(data), flags=re.MULTILINE|re.DOTALL),str(re.findall(r'<code>(.*?)</code>', str(data), flags=re.DOTALL))
def stripunc(data):
    return re.sub('[^A-Za-z]+', ' ', str(data), flags=re.MULTILINE|re.DOTALL)

stemmer = SnowballStemmer("english")

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/index')
def index():
    return flask.render_template('main.html')

@app.route('/predict', methods=['POST'])
def predict():
    
    data = request.form.to_dict()
    ttitle = data['q_title']
    tbody = data['q_body']
    '''
    review_text = clean_text(to_predict_list['review_text'])
    pred = clf.predict(count_vect.transform([review_text]))
    if pred[0]:
        prediction = "Positive"
    else:
        prediction = "Negative"
    return jsonify({'prediction': str(ttitle)})'''

    tbody,code = stripcode(tbody)
    tbody = str(ttitle)+" "+str(ttitle)+" "+str(ttitle)+" "+str(tbody)
    tbody = stripunc(tbody)
    words=word_tokenize(str(tbody.lower()))
    #Removing all single letter and and stopwords from question exceptt for the letter 'c'
    tbody=' '.join(str(stemmer.stem(j)) for j in words if j not in stop_words and (len(j)!=1 or j=='c'))

    Xq = vectorizer.transform([tbody])
    pred = clf.predict(Xq)
    pred_bool = pred.toarray()
    pred_bool = np.array(pred_bool)
    #print(len(pred_bool))
    #print(len(tag_list))
    #print(pred_bool)
    result = tag_list[pred_bool[0]>0]

    return jsonify({'prediction': str(result)})
    #return jsonify({'prediction': ['Test','Tester','Testest','Testester']})



if __name__ == '__main__':
    app.run(host='localhost', port=8999)