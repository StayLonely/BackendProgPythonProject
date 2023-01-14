import csv

with open('vacancies_with_skills.csv', newline= '', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    skill = {'PHP': 0, 'HTML': 0, 'CSS3': 0, 'JavaScript': 0, 'MySQL': 0, 'REST': 0, 'laravel': 0, 'lumen': 0, 'Slim': 0, 'Symfony': 0, 'Git': 0, 'Linux': 0, 'SQL': 0, 'PHP5': 0, 'Symfony2': 0, 'Ajax': 0, 'Python': 0, 'PostgreSQL': 0, '1С-Битрикс': 0, 'ООП': 0, 'Websockets': 0, 'Ruby': 0, 'TCP/IP': 0, 'iOS': 0, 'Swift': 0, 'Android': 0, 'Java': 0, 'Bash': 0, 'Nginx': 0, 'Node.js': 0, 'MongoDB': 0, 'Redis': 0, 'Docker': 0, 'API': 0, 'MS SQL': 0, 'Управление проектами': 0, 'Doctrine2': 0, 'PHP7': 0, 'Yii2': 0, 'Yii': 0, 'MVC': 0, 'ORM': 0, 'CSS': 0, 'jQuery': 0, 'Веб-программирование': 0, 'Разработка ПО': 0, 'Apache HTTP Server': 0, 'XML': 0, 'SVN': 0, 'Серверное программирование': 0, 'Google API': 0, 'CMS Wordpress': 0, 'Laravel': 0, 'RabbitMQ': 0, 'ORACLE': 0, 'Qt': 0, 'Atlassian Jira': 0, 'TeamCity': 0, 'Jenkins': 0, 'C#': 0, 'WPF': 0, 'WCF': 0, 'ASP.NET': 0, 'СУБД': 0, '.NET Framework': 0, 'Entity Framework': 0, 'LINQ': 0, 'Bootstrap': 0, 'JSON': 0, 'Scrum': 0, 'HTML5': 0, 'Symofny': 0, 'Composer': 0, 'Unit Testing': 0, 'PHPUnit': 0, 'TDD': 0, 'CI/CD': 0, 'SOLID': 0, 'IoC': 0, 'DI': 0, 'Spring Framework': 0, 'React.js': 0, 'vue.js': 0, 'Drupal API': 0, 'php7': 0, 'PSR': 0, 'Jetbrains Phpstorm': 0, 'SOAP': 0, 'CRM': 0, 'Artisan': 0, 'Eloquent': 0, 'Delphi': 0, 'FirebirdSQL': 0, 'Cистемы управления базами данных': 0, 'Design Patterns': 0, 'Собеседование': 0, 'Vue.js': 0, 'Angular.js': 0, 'Go': 0, 'опыт тестирования кода': 0, 'Базы данных': 0, 'Информационные технологии': 0, 'Техническая документация': 0, 'Работа в команде': 0, 'Joomla CMS': 0, 'C++': 0, '.NET': 0, 'Английский язык': 0, 'OpenCart': 0, 'rust': 0, 'docker': 0, 'flutter': 0, 'GraphQL': 0, 'Docker-compose': 0, 'Удаленная работа': 0, 'Postgres': 0, 'Умение работать в коллективе': 0, 'Backend': 0, 'Web Services': 0, 'Django Framework': 0, 'C/C++': 0, 'Unix': 0, 'Video': 0, 'solid': 0, 'Web': 0, 'back-end': 0, 'ПО': 0, 'HTTP': 0, 'Flask': 0, 'Hibernate ORM': 0, 'Python (backend)': 0, 'OpenStack': 0, 'Puppet': 0, 'Networking': 0, 'Multithreading': 0, 'h.264': 0, 'mp4': 0, 'mpeg-ts': 0, 'HLS': 0, 'Ruby On Rails': 0, 'REST API': 0, 'Facebook API': 0, 'Perl': 0, 'SCALA': 0, 'Sphinx': 0, 'Администрирование серверов Linux': 0, 'regexp': 0, 'RoR': 0, 'Erlang': 0, 'Lua': 0, 'Haskell': 0, 'reactjs': 0, 'react': 0, 'fullstack': 0, 'full stack': 0, 'redshift': 0, 'ETL': 0, 'Skype': 0, 'Rake tasks': 0, 'Delayed jobs': 0, 'Adobe Photoshop': 0, 'Шардинг': 0, 'Репликация': 0, 'Оптимизация БД': 0, 'Highload': 0, 'адекватность': 0, 'Objective-C': 0, 'aosp': 0, 'swift': 0, 'backend': 0, 'PCI DSS': 0, 'acquiring': 0, 'Zend Framework': 0, 'bitbucket': 0, 'Trello': 0, 'No SQL': 0, 'Scala, JavaScript , C++/JNI, PHP, Ruby (ROR)': 0, 'Big Data': 0, 'Hadoop': 0, 'Codeigniter': 0, 'Microsoft Visual Studio': 0, 'Azure': 0, 'Xamarin': 0, 'SQL Server': 0, 'ReactJS': 0, 'AngularJS': 0, 'knockoutJS': 0, 'Typescript': 0, 'ADO.NET': 0, 'JS': 0, 'Ubuntu Server': 0, 'ElasticSearch': 0, 'Lumen': 0, 'Angular2': 0, 'Golang': 0, 'Асинхронное программирование': 0, 'Bitrix': 0, 'WEB': 0, 'Битрикс24': 0, 'Битрикс': 0, 'Bitrix framework': 0, 'BPM': 0, 'мозг': 0, 'любить программировать': 0, 'parse.com': 0, 'MS SQL Server': 0, 'MS Visual Studio': 0, 'QA': 0, 'Magento': 0, 'E-Commerce': 0, 'python 2': 0, 'scrapy': 0, 'OAuth2': 0, 'Web Application Development': 0, 'Шаблоны проектирования': 0, 'i18n': 0, 'MS Visual Studio 2013': 0, 'Slack': 0, 'JSON API': 0, 'Net Framework 4.5': 0, 'C# 5.0': 0, 'MSTest': 0, 'NUnit': 0, 'ownCloud': 0, 'AWS': 0, 'Java SE': 0, 'Проектирование баз данных': 0, 'Железнодорожные перевозки': 0, 'Backend Java-разработчик': 0, 'Redmine': 0, 'LAMP': 0, 'Memcached': 0, 'STL': 0, 'XML/Xslt': 0, 'golang': 0, 'VBA': 0, 'Создание сайтов': 0, 'Ответственность': 0, 'Дисциплинированность': 0, 'NoSQL': 0, 'Business English': 0, 'Agile': 0, 'Computer science': 0, 'автоматизация тестирования': 0, 'Тестирование': 0, 'ООП Java SQL': 0, 'ffmpeg': 0, 'Framework': 0, 'Tornado': 0, 'Mercurial': 0, 'D7': 0, 'high-load': 0, 'DevOPS': 0, 'Sinatra': 0, 'Amazon AWS': 0, 'Groovy': 0, 'Selenium IDE': 0, 'Jmeter': 0, 'KVM': 0, 'libvirt': 0, 'Go-lang': 0, 'React Native': 0, 'Atlassian Confluence': 0, 'UML': 0, 'Multithread Programming': 0, 'yii php': 0, 'NoSQL базы данных': 0, 'PHP, OOP, HTML, CSS': 0, 'business-thinker': 0, 'Тестирование пользовательского интерфейса': 0, 'Проведение тестирований': 0, 'Регресcионное тестирование': 0, 'Bug Tracking Systems': 0, 'Test case': 0, 'Автоматизация': 0, 'Постановка задач разработчикам': 0, 'верстальщик': 0, 'программист': 0, 'SEO': 0, 'Администрирование серверов Windows': 0, 'ActiveRecord': 0, 'jQuery.ui': 0, 'MySql 5': 0, 'HTTP/1.1': 0, 'Framework Symfony 2': 0, 'Framework Symfony': 0, 'Kohana': 0, 'Стрессоустойчивость': 0, 'Аналитический склад ума': 0, 'Исполнительность': 0, 'JMM': 0, 'Concurrency': 0, 'Collections': 0, 'Oracle Pl/SQL': 0, 'Apache Tomcat': 0, 'JSF': 0, 'Оптимизация запросов': 0, 'oAuth': 0, 'go': 0, 'phyton': 0, 'Креативность': 0, 'Transact-SQL': 0, 'Windows Forms': 0, 'Ориентация на результат': 0, 'Backbone': 0, 'Goland': 0, 'Devops': 0, 'Restful api': 0, 'ClickHouse': 0, 'IQ option': 0, 'Unity': 0, 'Ruby 2.1+; Rails 4.1+; БД PostgreSQL, Cassandra, Redis; RabbitMQ; Скрипты на Ruby': 0, 'ERP Systems': 0, 'ERP': 0, 'React': 0, 'cython': 0, 'numpy': 0, 'pandas': 0, 'Архитектура': 0, 'pypy': 0, 'elastic search': 0, 'ES6': 0, 'JPA': 0, 'Функциональное тестирование': 0, 'тестирование приложений': 0, 'BigQuery': 0, 'Голова на плечах': 0, 'Руки откуда надо': 0, 'Сложно': 0, '.NET Web API': 0, 'DevOps': 0, 'vuejs': 0, 'Ant, Maven': 0, 'ASP.NET Core': 0, 'TypeScript': 0, 'браузерные API': 0, 'DOM': 0, 'Prototype Js': 0, 'Lisp': 0, 'F#': 0, 'Clojure': 0, 'OСaml': 0, 'Elasticsearch': 0, 'gevent': 0, 'SQL Server Express': 0, 'Python3': 0, 'momoko': 0, 'Управление персоналом': 0, 'AMQP': 0, 'Websocket': 0, 'SaaS': 0, 'YII2': 0, 'Управление командой': 0, 'Лидерские качества': 0, 'Разработка технических заданий': 0, 'Разработка и внедрение политик и процедур': 0, 'руководство командой разработчиков': 0, 'Agile Project Management': 0, 'Jira': 0, '.net core': 0, 'highload': 0, 'Game Programming': 0, 'IIS': 0, 'tornado': 0, 'Twisted': 0, 'php 7': 0, 'Работа с SQL': 0, 'MySQL, PostgreSQL': 0, 'NoSQL СУБД': 0, 'Unix/Linux': 0, 'PHP разработчик': 0, 'backend/api': 0, 'Lambda': 0, 'S3': 0, 'Gamedev': 0, 'Spring': 0, 'Akka': 0, 'aerospike': 0, 'IT Recruitment': 0, 'Администрирование сайтов': 0, 'Codeception': 0, 'Postman': 0, 'Модульное тестирование': 0, 'Интеграционное тестирование': 0, 'Автоматизация тестирования': 0, 'express.js': 0, 'Express.js': 0, 'IBM': 0, 'Bank Software': 0, 'Микросервисная архитектура': 0, 'Sass': 0, 'Web API': 0, 'ServiceStack': 0, 'NancyFX': 0, 'yii2': 0, 'Postfix': 0, 'Dovecot': 0, 'Настройка DNS': 0, 'Pyramid': 0, 'SQLAlchemy': 0, 'Celery': 0, 'Woocommerce': 0, 'Высоконагруженные системы': 0, 'Создание архитектуры проектов': 0, 'Backend development': 0, 'Amazon aws': 0, 'Знание платформы Microsoft .NET, ASP.NET, ASP.NET MVC, WCF, LINQ': 0, 'Опыт веб-разработки в коммерческих проектах': 0, 'Уверенное владение С#': 0, 'Знание и практический опыт разработки веб-интерфейсов (HTML, CSS, JavaScript, Angular в т.ч. jQuery': 0, 'Опыт проектирования и разработки под промышленную СУБД (Oracle / Postgres);': 0, 'Разработка CMS': 0, 'mssql': 0, 'реляционные базы данных': 0, 'yii 2': 0, 'Phalcon': 0, 'Back End': 0, 'С#': 0, 'framework': 0, 'Java NIO': 0, 'Rest API': 0, 'Netty': 0, 'AWT': 0, 'agile': 0, 'postgresgl': 0, 'Node': 0, 'JSP': 0, 'Apache Maven': 0, 'Distributed systems': 0, '.NET Core': 0, 'aspose': 0, 'aws': 0, 'Системная интеграция': 0, 'Clickhouse': 0, 'Kubernetes': 0, 'Continuous Integration': 0, 'Continuous Delivery': 0, 'С11': 0, 'Python 3': 0, 'High Load': 0, 'Multithreaded Applications': 0, 'blockchain': 0, 'amazon aws': 0, 'rest api': 0, 'paypal': 0, 'stripe': 0, 'framework laravel': 0, 'NHibernate': 0, 'GO': 0, 'Swift для iOS': 0, 'React для Android': 0, 'JVM': 0, 'RxJava': 0, 'Spark': 0, 'Code review': 0, 'unit-тесты': 0, 'JIRA': 0, 'РСУБД': 0, 'Selenium webdriver': 0, 'Нагрузочное тестирование': 0, 'LLVM': 0, 'Rust': 0, 'Forth': 0, 'celery': 0, 'microservice architecture': 0, 'Dev Ops': 0, 'Блочная верстка': 0, 'backend developemnt': 0, 'analytics': 0, 'marketing': 0, 'Информационная безопасность': 0, '152 ФЗ': 0, 'разработка нормативных документов': 0, 'Databases': 0, 'MariaDB': 0, 'sf2': 0, 'sf3': 0, 'tarantool': 0, 'Troubleshooting': 0, 'clickhouse': 0, 'Riak': 0, 'ExpressJS': 0, 'heroku': 0, 'DRY, KISS, SOLID': 0, 'TDD, BDD, DDD': 0, 'всё равно никто не читает теги': 0, 'NLP': 0, 'Bot Development': 0, 'Stream Voice Processing': 0, 'Желание обучаться!': 0, 'Знание Ruby on Rails': 0, 'Опыт работы c PostgreSQL': 0, 'GitLab': 0, 'GitHub': 0, 'MODx': 0, 'Java Virtual Machine': 0, 'Docer': 0, 'Visual Studio C#': 0, 'Nats': 0, 'CentOS': 0, 'Performance': 0, 'База данных: Oracle': 0, 'kohana': 0, 'Symfony 3': 0, 'Doctrine': 0, 'RabbitMQ,': 0, 'SCSS': 0, 'Bootstrap 4': 0, 'Blockchain': 0, 'spring boot': 0, 'spring cloud': 0, 'Prestashop CMS': 0, 'Opencart': 0, 'Кроссбраузерная верстка': 0, 'мобильная версия': 0, 'Hypersonic Sql': 0, 'HighLoad': 0, 'Kotlin': 0, 'Redux': 0, 'Django': 0, 'CorelDRAW': 0, 'Adobe InDesign': 0, 'typescript': 0, 'мониторинг ЦОД': 0, 'aiohttp': 0, 'High load applications': 0, 'руки из плеч': 0, 'MMO RPG': 0, 'JDBC': 0, 'Java EE': 0, 'stream api': 0, 'jdk': 0, 'Разработка компьютерных Игр': 0, 'компьютерные игры': 0, 'понимание бизнес-логики': 0, 'синергия': 0, 'Sharding': 0, 'green threads': 0, 'GIS': 0, 'Polymer': 0, 'MS SQL 2008': 0, 'Sailfish': 0, 'phalconphp': 0, 'Beanstalk': 0, 'Ext JS': 0, 'D3.js': 0, 'Vuejs': 0, 'Rabbit MQ': 0, 'Yii 2.0': 0, 'AngularJs 6': 0, 'Gulp': 0, 'Less': 0, 'Cassandra': 0, 'Yii framework': 0, 'VCS': 0, 'Django Rest Framework': 0, 'DRF': 0, 'elasticsearch': 0, 'Back end': 0, 'Symfony 2/3': 0, 'php 5': 0, 'java script': 0, '*nix shell': 0, 'MS Excel': 0, 'ModX': 0, 'Windows': 0, 'Автоматизированное тестирование': 0, 'XQuery': 0, 'Drupal как с CMF': 0, 'angular': 0, 'PaaS': 0, 'Smarty': 0, 'Java Servlets': 0, 'EJB': 0, 'TFS': 0, 'Teamleading': 0, 'Внимательность': 0, 'Коммуникабельность': 0, 'RestAPI': 0, 'Development': 0, 'RESTful API': 0, 'angular4': 0, 'Spring Boot': 0, 'Apache Ignite': 0, 'Apache Cassandra': 0, 'Яндекс ClickHouse': 0, 'HAproxy': 0, 'Apache Solr': 0, 'алгоритмы': 0, 'структуры данных': 0, 'Java Spring MVC': 0, 'Maven': 0, 'RDBMS': 0, 'Gradle': 0, 'Java 8': 0, 'Микросервисы': 0, 'Core Java': 0, 'Классические алгоритмы': 0, 'Распределенные системы': 0, 'JavaDoc': 0, 'BI': 0, 'Intellij IDEA': 0, 'Kanban': 0, 'SOAP Web Services': 0, 'TFS 2015': 0, 'modified condition decision coverage': 0, 'HP QC/ SM': 0, 'Visual Studio Code': 0, 'Black box testing': 0, 'White box testing': 0, 'Разработка нового продукта': 0, 'Оптимизация бизнес-процессов': 0, 'Pl/Python': 0, 'Опыт работы с платформой .NET (3.5-4.0).': 0, 'Опыт работы с СУБД: mySQL/postgreSQL.': 0, 'Использование SVN.': 0, 'WCF, LINQ, XML': 0, 'опыт работы с системами отчетов': 0, 'Телеметрия в автотранспорте': 0, 'Большие данные (Big data)': 0, 'Опыт в GPS /ГЛОНАС': 0, 'Удалённый контроль объектов в автотрансопрте/ логистика': 0, 'опыт работы с системами очередей': 0, 'Программист С#': 0, 'Разработчик': 0, 'VueJs': 0, 'jvm': 0, 'Tarantool': 0, 'Mac Os': 0, 'MS Visual C++': 0, 'Managed C++': 0, 'SQLite': 0, 'Работа с базами данных': 0, 'Экстремальное программирование': 0, 'Многопоточное программирование': 0, 'Software Development': 0, 'QuickFIX': 0, 'Kubernetus': 0, 'Elastick Stack': 0, 'Nuts': 0, 'Рефакторинг кода': 0, 'Zephir': 0, 'Lxc': 0, 'Rancher': 0, 'Программирование PHP7': 0, 'Программное обеспечение Backend Developer': 0, 'Backend Engineer': 0, 'Backend PHP': 0, 'web development': 0, 'raiden': 0, 'solidity': 0, 'webAssembly': 0, 'swagger': 0, 'JUnit': 0, 'opencart': 0, 'Networking, TCP / UDP': 0, 'Web-программист': 0, 'Адаптивная верстка': 0, 'Структуры данных': 0, 'ISP/domain specific': 0, 'Ansible': 0, 'Apache Kafka': 0, 'Terraform': 0, 'Boost': 0, 'modx': 0, 'Оптимизация кода': 0, 'Middle backend': 0, 'Middle PHP': 0, 'backend АБС': 0, 'АБС': 0, 'CS-cart': 0, 'Kibana': 0, 'Grafana': 0, 'Fintech': 0, 'Финтехпроект': 0, 'БАНК131': 0, 'Онлайн-банк': 0, 'Symfony4': 0, 'Gitlab': 0, 'Logstash': 0, 'Thrift': 0, 'logstash': 0, 'prometheus': 0, 'Packagist': 0, 'Паттерны проектирования': 0, 'Опыт тестирования': 0, 'Удаленное сотрудничество': 0, 'продуктовая разработка': 0, 'akka': 0, 'protobuf': 0, 'netty': 0, 'akka streams': 0, 'Graph QL': 0, 'Sream API': 0, 'mapreduce': 0, 'SOAP-XML, SOAP-JSON, JSON-RPC': 0, 'ручное тестирование': 0, 'стресс-тестирование': 0, 'Angular': 0, 'RSpec': 0, 'Capistrano': 0, 'mocha': 0, 'Amazon': 0, 'CPA': 0, 'Gillab': 0, 'Restful': 0, 'Проектирование': 0, 'Team management': 0, 'gearman': 0, 'Регресионное тестирование': 0, 'интеграционное тестирование': 0, 'Пользователь ПК': 0, 'ASP.NET MVC': 0, 'ASP.NET WEB API': 0, 'C#7.0': 0, 'VS2017': 0, 'NSQ': 0, 'WCF services': 0, 'Postgress/Mongo': 0, 'Обучение и развитие': 0, 'GITHUB': 0, 'Документирование': 0, 'Скорость разработки': 0, 'Читабельный код': 0, 'Vue': 0, 'Hiera': 0, 'Scribe': 0, 'Zabbix': 0, 'Zookeeper': 0, 'Debian': 0, 'SRE': 0, 'Apollo': 0, 'Shell Scripting': 0, 'test automation': 0, 'Администрирование': 0, 'Web Design': 0, 'Full stack': 0, 'gRPC': 0, 'NATS': 0, 'Sidekiq': 0, 'GoLang': 0, 'elas': 0, 'Java Core (8)': 0, 'Написание Unit-тестов': 0, 'RocksDB': 0, 'asyncio': 0, 'sanic': 0, 'peewee': 0, 'Управленческие навыки': 0, 'python, django, wsgi, gunicorn, postgresql, git, redis': 0, 'Modx Revolution': 0, 'CMS 1С Битрикс': 0, 'программист php': 0, 'микросервисы': 0, 'frontend': 0, 'Frontend': 0, 'AutoCAD': 0, 'Sequelize': 0, 'Express': 0, 'Testing Framework': 0, 'load testing': 0, 'парсер': 0, 'Data Mining': 0, 'Eclipse': 0, 'NetBeans': 0, 'MS SharePoint': 0, 'Laravel 5': 0, 'automation': 0, 'software development testing': 0, 'web-разработка': 0, 'vue': 0, 'socket.io': 0, 'FIX protocol': 0, 'MT4': 0, 'MetaTrader': 0, 'Cryptocurrency': 0, 'ZeroMQ': 0, 'ICO': 0, 'Веб-дизайн': 0, 'Web-дизайн': 0, 'Анализ данных': 0, 'Сбор и анализ информации': 0, 'Аналитика': 0, 'Аналитическое мышление': 0, 'backend-разработчик': 0, 'VueJS': 0, 'Переквалификация': 0, 'холодная голова, горячее сердце, чистые руки': 0, 'NetCore': 0, 'NetStandart': 0, 'EntityFrameworkCore 2.1': 0, 'ServiceStack 5': 0, '.NET (C#, WebAPI, .Net Core); шаблоны проектирования, SOLID; MS SQL; Entity Framework': 0, 'Лидерство': 0, 'Управление временем': 0, 'SPA': 0, 'BPMN': 0, 'Верстка': 0, 'cassandra': 0, 'kafka': 0, 'MySQL jQuery Git Ajax CSS3 ООП HTML PHP7 Yii': 0, 'bitrix': 0, 'Kafka': 0, 'Apache': 0, '.Net': 0, 'Google Cloud': 0, 'swager': 0, 'Организация рабочих мест': 0, 'Материальная ответственность': 0, 'Elastic Search': 0, 'DynamoDB': 0, 'Поддержка кода других программистов': 0, 'asp .net core': 0, 'Nest.js': 0, 'Prisma': 0, 'API Platform': 0, 'Apache Flex': 0, 'Code revier': 0, 'Vuex': 0, 'Nuxt': 0, 'Java Spring Framework': 0, 'Oracle DB': 0, 'NixOS': 0, 'PHP MySQL HTML CSS JavaScript': 0, 'Управление разработкой': 0, 'Vagrant': 0, 'Software Development Life Cycle Methodologies': 0, 'Javascript (Nginx, node.js, React, vue) and PHP': 0, 'SQL and NOSQL databases': 0, 'ANT': 0, 'Международные контакты': 0, 'Ionic 4': 0, 'Native': 0, 'Gybrid': 0, 'MQTT': 0, 'Grails': 0, 'Наставничество': 0, 'Опыт управления командой': 0, 'Nest.Js': 0, 'WSDL': 0, 'Бизнес-анализ': 0, 'Type Script': 0, 'PetaPoco': 0, 'Elmah': 0, 'backend QA': 0, 'Vert.x': 0, 'Bitrix24': 0, 'Teambuilding': 0, 'EOS': 0, 'Ethereum': 0, 'web сервер': 0, 'desktop': 0, 'twilio': 0, 'amazonaws': 0, 'dropwizard': 0, 'bouncycastle': 0, 'protobuf-java': 0, 'jersey': 0, 'CQRS': 0, 'Оптимизация кода PHP Python HTML Java Script CSS MySQL': 0, 'APIРазработка продукта': 0, 'Автоматизация продаж': 0, 'Торговый маркетинг': 0, 'Автоматизация технологических процессов': 0, 'пунктуальность': 0, '1С: Розница': 0, 'Корпоративная этика': 0, 'Docker Compose': 0, 'PHP 7': 0, 'PowerShell': 0, 'express': 0, 'Hive': 0, 'Data Warehouse': 0, 'Github': 0, 'OpenSource': 0, 'Реализация внутреннего и публичного API для взаимодействия с мобильными приложениями и front-end': 0, 'Разработка различных сервисов, в том числе по обработке событий (уведомлений).': 0, 'Участие в проектировании API и БД совместно с архитектором.': 0, 'Хорошее знание реляционных БД (MySQL, PostgreSQL)': 0, 'Работа с системами контроля версий (svn).': 0, 'Опыт разработки в команде.': 0, 'Приветствуется знание фреймворка lumen': 0, 'Опыт реализации и поддержки больших/сложных проектов.': 0, 'Yii 2': 0, 'криптография': 0, 'WebAssembly': 0, 'DLT': 0, 'SOLID Docker Git DBMS ООП': 0, 'VUE': 0, 'PHALCON': 0, 'PHALCON FRAMEWORK': 0, 'ActiveMQ': 0, 'виртуализация': 0, 'краулинг': 0, 'cURL': 0, 'Socket.io': 0, 'DBMS': 0, 'XPath': 0, 'FTP': 0, 'MS Azure': 0, 'kubernetes': 0, 'Pascal': 0, 'MS Access': 0, 'знание NLP (Natural Language Processing)': 0, 'Умение работать в команде': 0, 'неординарность мышления': 0, 'активность': 0, 'трудолюбие': 0, 'Инициативность': 0, 'внимательность': 0, 'Wowza': 0, 'Средства криптографической защиты информации': 0, 'DDD': 0, '.NET CORE': 0, 'azure': 0, 'pytest': 0, 'locust': 0, 'Stock market': 0, 'Алготрейдинг': 0, 'Algotrading': 0, 'Психология': 0, 'Ведение переговоров': 0, 'Организаторские навыки': 0, 'Wagtail': 0, 'October': 0, 'TypeScript/Javascript': 0, 'Microservice architecture': 0, 'Gzip': 0, 'Deflate': 0, 'Htaccess': 0, 'Apache Hadoop': 0, 'laravel php': 0, 'REST/JSON': 0, 'Работа с большим объемом информации': 0, 'Внутренний контроль': 0, 'AllFusion ERwin Data Modeler': 0, 'Мобильность': 0, 'PostreSQL': 0, 'ES2015+': 0, 'JSON-RPC': 0, 'Koa.js': 0, 'Web Soсkets': 0, 'End2End': 0, 'Приемочное тестирование': 0, 'MangoDB': 0, 'RESTAPI': 0, 'vue js': 0, 'phpMyAdmin': 0, 'vagrant': 0, 'Jasper Reports': 0, 'Организация мероприятий': 0, 'инфраструктура': 0, 'облачные технологии': 0, 'Manage IQ': 0, 'оркестраторы': 0, 'CloudForms': 0, 'Typing': 0, 'беспилот': 0, 'серверные комп': 0, '*NIX': 0, 'open cart': 0, 'Продажи через интернет': 0, 'IT': 0, 'Мотивация': 0, 'Ubuntu': 0, 'ROS': 0, 'Многозадачность': 0, 'Автоматизация процессов': 0, 'JavaEE': 0, 'B2B маркетинг': 0, 'E-Mail Marketing': 0, 'Start-up project': 0, 'Системы видеонаблюдения': 0, 'Сопровождение строительства': 0, 'слаботочные системы': 0, 'Email маркетинг': 0, 'маркетинг': 0, 'Холодные продажи': 0, 'презентация': 0, 'keynote': 0, 'MS PowerPoint': 0, 'Рассылка сообщений': 0, 'Техники продаж': 0, 'Литературная деятельность': 0, 'Cоциальный маркетинг': 0, 'Активные продажи': 0, 'Управление отношениями с клиентами': 0, 'Деловая коммуникация': 0, 'Webpack': 0, 'Vue JS': 0, 'Google Chrome': 0, 'Telegram': 0, 'SpringBoot': 0, 'Стратегическое мышление': 0, 'postgres': 0, 'sphinxsearch': 0, 'gitlab': 0, 'Senior': 0, 'Middle': 0, '1c': 0, 'get.': 0, 'lavarel': 0, 'Немецкий язык': 0, 'Аналитические способности': 0, 'Разработка концепции': 0, 'JMS': 0, 'OOP': 0, 'OpenAPI': 0, 'Системный анализ': 0, 'DRY': 0, 'YAGNI': 0, 'Backend-разработка': 0, 'typescipt': 0, 'graphql': 0, 'webview': 0, 'Core WebApi': 0, 'Amazon Web Services': 0, 'Северное программирование': 0, 'экстримальное программирование': 0, 'Developer Express': 0, 'Requery': 0, 'Математический анализ': 0, 'jetbrains YouTrack': 0, 'Net': 0, 'net.core': 0, 'OrmLite': 0, 'SQL 2017': 0, 'web': 0, 'Maria DB': 0, 'Ответственность и умение работать по стандартам.': 0, 'Rx': 0, 'Rabbit': 0, 'Graphana': 0, 'ELK': 0, 'C# 8': 0, '.Net core': 0, 'PostgresDB': 0, 'Cloudera': 0, 'PyTest': 0, 'Presentation skills': 0, 'Pytest': 0, 'Oracle Application Server': 0, 'Криптография': 0, 'Транспортная логистика': 0, 'sqlalchemy': 0, 'MQ': 0, 'UX': 0, 'Проектирование архитектуры': 0, 'kotlin': 0, 'PL/pgSQL': 0, 'middle': 0, 'webpack': 0, 'Cucumber': 0, 'jmeter': 0, 'интернет-магазин': 0, 'разработка': 0, 'Средний (Middle)': 0, 'CMS Drupal': 0, 'Доработка функционала': 0, 'Техподдержка': 0, 'Разработка мобильных приложений': 0, 'службы Windows Service': 0, 'multithreading': 0, 'spider': 0, 'parsing': 0, 'proxy': 0, 'IoT': 0, 'Spring boot': 0, 'NET Core C#': 0, 'RESTful': 0, 'WebSoket': 0, 'net core': 0, '.Net Core': 0, 'react.js': 0, 'шарпоинт': 0, 'C# разработчик': 0, 'back end': 0, 'веб-сервис': 0, 'NET Framework 4.0': 0, 'T-SQL': 0, 'Организационное проектирование': 0, 'Системный подход': 0, 'graphQL': 0, 'Turbo Pascal': 0, 'NodeJS': 0, 'Opera': 0, 'Angular 7': 0, 'Обучение': 0, 'реляционные БД': 0, 'проектирование API': 0, 'работа с микросервисной архитектурой': 0, 'Грамотная речь': 0, 'Грамотность': 0, 'Scrapy': 0, 'Парсинг': 0, 'Системное мышление': 0, 'ОС Linux': 0, '• Желание развиваться профессионально': 0, 'Couchbase': 0, 'ECDSA': 0, 'yii1, PHP 7.1, mysql 5.5': 0, 'CMS': 0, 'Обучение персонала': 0, 'Microservices': 0, 'UDP': 0, 'Native PHP': 0, 'Программирование': 0, 'LARAVEL': 0, 'KOTLIN': 0, 'разработка сайтов': 0, 'php 7+': 0, 'GitLab CI/CD': 0, 'Android SDK': 0, 'iveQL': 0, 'Graylog': 0, 'fintech': 0, 'финтех': 0, 'Go Lang': 0, 'Grasp': 0, 'Project management': 0, 'Time management': 0, 'Первичные документы': 0, 'jMeter': 0, 'PDF': 0, 'Преобразование данных': 0, 'Интеграция': 0, 'PHP73': 0, 'lighttpd': 0, 'Xsd': 0, 'Terrasoft CRM': 0, 'shell': 0, 'Проектная документация': 0, 'Валидная верстка': 0, 'адаптивная верстка': 0, 'Figma': 0, 'Back-end': 0, 'Quasar framework': 0, 'Работа с клиентами': 0, 'TTL': 0, 'Graphite': 0, 'Configuration Management': 0, 'GitLab CI': 0, 'Flash MySQL': 0, 'Logs management': 0, 'ELK stack': 0, "Let's Encrypt": 0, 'DynDNS': 0, 'Prometheus': 0, 'VPN': 0, 'Microsoft HyperV': 0, 'Sendgrid': 0, 'Опыт работы backend': 0, 'Sphinxsearch': 0, 'CMS Битрик': 0, 'Unix Shell Scripts': 0, 'MS Outlook': 0, 'Cjdeception': 0, 'Планирование карьеры': 0, 'Веб-разработка': 0, 'aнглийский язык': 0, 'Основы WEB программирования': 0, 'Leflet': 0, 'Организация конференций': 0, 'OctoberCMS': 0, 'Vue js': 0, '*nix': 0, 'Xdebug': 0, 'webSocket': 0, 'mobile app': 0, 'Архитектура ПО': 0, 'IDEF0': 0, 'IDEF': 0, 'JBoss Enterprise': 0, 'Английский — B1 — Средний': 0, 'Visual Studio 2019': 0, 'Design Patterns (GoF)': 0, 'EDA': 0, 'PHP 8': 0, 'Open Api': 0, 'серверы приложений': 0, 'серверы': 0, 'системы платежей': 0, 'машинное обучение': 0, 'Системы идентификации и аутентификации': 0, 'сквозное шифрование': 0, 'передача видео': 0, 'BigCommerce': 0, 'Расстановка приоритетов': 0, 'Командная разработка': 0, 'Reddis': 0, 'postman': 0, 'Django, REST API': 0, 'PHP 7, REST': 0, 'SOLID.': 0, 'threading': 0, 'WIndows Phone': 0, 'Mass Transit': 0, 'CORS': 0, 'web Api': 0, 'Организация семинаров': 0, 'Умение принимать решения': 0, 'Общественное питание': 0, 'Точность и внимательность к деталям': 0, 'Руководство коллективом': 0, 'signalr': 0, 'Solid Edge': 0, 'amazone S3': 0, '.NET core': 0, 'C': 0, 'Product Management': 0, 'Windows 7': 0, 'GoF': 0, 'authentication methods': 0, 'e2e testing': 0, 'игры': 0, 'nodejs': 0, 'js': 0, 'node': 0, 'GDAL': 0, 'goLang': 0, 'ssl': 0, 'YouTrack': 0, 'bullmq': 0, 'Управление талантами': 0, 'elasticseach': 0, 'Клиентоориентированность': 0, 'Asterisk': 0, 'SIP': 0, 'Oracle Database': 0, 'SQL Navigator': 0, 'Высоконагруженный клиентский сервис': 0, 'самообучение': 0, 'Подготовка презентаций': 0, 'Проведение презентаций': 0, 'Java11': 0, 'АРI': 0, 'Splunk': 0, 'SOAPUI': 0, 'JMETER': 0, 'WebSockets': 0, 'Сообразительность': 0, 'Битрикс 24': 0, 'Настройка VPS/VDS серверов': 0, 'MSSQL': 0, 'EntityFramework': 0, 'Unity (IoC)': 0, 'ASP.NET Core 3.1': 0, 'InfluxDB': 0, 'Quartz.NET': 0, 'EasyNetQ': 0, 'AppMetrics': 0, 'Protobuf': 0, 'crypto': 0, 'ai': 0, 'NestJs': 0, 'Notion': 0, 'Дружелюбие': 0, 'Работа в условиях многозадачности': 0, 'FastAPI': 0, 'Криптовалюта': 0, 'Pandas': 0, 'Numpy': 0, 'Google Analytics': 0, 'Яндекс.Директ': 0, 'Веб-аналитика': 0, 'Интернет-реклама': 0, 'Яндекс.Метрика': 0, 'microservices': 0, 'NewRelic': 0, 'Serverless': 0, 'django': 0, 'С++': 0, 'gitflow': 0, 'Java 11': 0, 'Amazon SQS': 0, 'NestJS': 0, 'Разработка продукта': 0, 'Product Development': 0, 'Точность': 0, 'Соблюдение сроков': 0, 'TestRail': 0, 'QA Automation': 0, 'Selenium': 0, 'Алгоритмы': 0, 'MacOS': 0, 'Умение слушать': 0, 'Stripe': 0, 'Gitlab CI': 0, 'Vertica': 0, 'EFK': 0, 'Sentry': 0, 'K8s': 0, 'ML': 0, 'AI': 0, 'Mathematical Programming': 0, 'Mathematical Modeling': 0, 'Поисковые системы': 0, 'Организационные навыки': 0, 'KANBAN': 0, '.netCore': 0, 'CI': 0, 'Блокчейн': 0, 'Желание учиться и развиваться': 0, 'MSSQL/ Redis': 0, 'Teamplayer': 0, 'Elm': 0, 'PureScript': 0, 'Elixir': 0, 'FP': 0, 'Функциональное программирование': 0, 'Аналитические навыки': 0, 'Критически мыслить': 0, 'Высокая скорость работы': 0, 'Высокая скорость печати': 0, 'Citrix': 0, 'Citrix Systems': 0, 'Сетевые технологии': 0, 'EF Core': 0, 'ESB': 0, 'MODX': 0, 'CMS MODX': 0, 'Базовые знания HTML': 0, 'k8s': 0, 'Java Script': 0, 'Самостоятельная работа': 0, 'Spring Cloud': 0, 'Mongo DB': 0, 'Hazelcast IMDG': 0, 'Solidity': 0, 'Смарт - контракты': 0, 'BPMS': 0, 'Hibernate': 0, 'Spring Data': 0, 'Liquibase': 0, 'xUnit': 0, 'NET Core': 0, 'NET': 0, 'Next.js': 0, 'Стремление к профессиональному росту': 0, 'RageMP': 0, 'ES': 0, 'Symphony': 0, 'Java 17': 0, 'High availability': 0, 'JS, Angular, React, C#, Java': 0, 'Русский язык': 0, 'HTML/CSS': 0, 'JSON:API': 0, 'fastapi': 0, 'Manual Testing': 0, 'Ручное тестирование': 0, 'Bug Reporting': 0, 'Zephyr': 0, 'Confluence': 0, 'алгоритмы и структуры данных': 0, 'grafana': 0, 'nest': 0, 'nest.js': 0, 'devops': 0, 'разработчик': 0, '12 factor app': 0, 'Желание обучаться': 0, 'Стремление к профессиональному развитию': 0, 'BDD': 0, 'SSH': 0, 'Gokit': 0, 'Go gin': 0, 'Golang.Org': 0, '1С программирование': 0, '1С: Предприятие 8': 0, 'Java backend': 0, 'Телекоммуникации': 0, 'websockets': 0, 'Смекалка': 0, 'Самообучение': 0, 'Самоменеджмент': 0, 'CS-Cart': 0, 'camunda': 0, 'neo4j': 0, 'spiring': 0, 'boot': 0, 'React/Redux': 0, 'type script': 0, 'auto test': 0, 'Business Strategy': 0, 'Accounting': 0, 'Hyperleger Fabric': 0, 'Управление процессами': 0, 'Ответственность и пунктуальность': 0, 'Знание английского': 0, 'Умение работать самостоятельно': 0, 'Выполнение поставленных задач': 0, 'Tensorflow': 0, 'OpenCV': 0, 'Опытный пользователь ПК': 0, 'Microsoft Office FrontPage': 0, 'Vkontakte Api': 0, 'Microsoft Access': 0, 'backend разработка': 0, 'SoapUI': 0, 'MS Dos': 0, 'nestjs': 0, 'typeorm': 0, 'вебсокеты, socket.io': 0}
    for row in reader:
        if ('backend-программист' in str(row['name']) or 'Backend-программист' in str(row['name']) \
                or 'backend' in str(row['name']) or 'бэкэнд' in str(row['name']) \
                or 'бэкенд' in str(row['name']) or 'бекенд' in str(row['name']) \
                or 'бекэнд' in str(row['name']) or 'back end' in str(row['name']) \
                or 'бэк энд' in str(row['name']) or 'бэк енд' in str(row['name']) \
                or 'django' in str(row['name']) or 'flask' in str(row['name']) \
                or 'symfony' in str(row['name']) or 'laravel' in str(row['name']) or 'yii' in str(row['name'])):
            if(len(row['key_skills']) > 0 and str(row['published_at'][:4]) == '2012'):
                skills = row['key_skills'].split('\n')

                for i in skills:
                    skill[i] += 1

res = dict(sorted(skill.items(), key=lambda x: -x[1]))


a = 0
for i in res:
    if(a > 10):
        break
    else:
        a+=1
        print(i, res[i])