{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: psycopg2-binary in c:\\users\\kede\\anaconda3\\lib\\site-packages (2.8.4)\n"
     ]
    }
   ],
   "source": [
    "!pip install psycopg2-binary"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "['BINARY',\n",
       " 'Binary',\n",
       " 'DATETIME',\n",
       " 'DataError',\n",
       " 'DatabaseError',\n",
       " 'Date',\n",
       " 'DateFromTicks',\n",
       " 'Error',\n",
       " 'IntegrityError',\n",
       " 'InterfaceError',\n",
       " 'InternalError',\n",
       " 'NUMBER',\n",
       " 'NotSupportedError',\n",
       " 'OperationalError',\n",
       " 'ProgrammingError',\n",
       " 'ROWID',\n",
       " 'STRING',\n",
       " 'Time',\n",
       " 'TimeFromTicks',\n",
       " 'Timestamp',\n",
       " 'TimestampFromTicks',\n",
       " 'Warning',\n",
       " '__builtins__',\n",
       " '__cached__',\n",
       " '__doc__',\n",
       " '__file__',\n",
       " '__libpq_version__',\n",
       " '__loader__',\n",
       " '__name__',\n",
       " '__package__',\n",
       " '__path__',\n",
       " '__spec__',\n",
       " '__version__',\n",
       " '_connect',\n",
       " '_ext',\n",
       " '_json',\n",
       " '_psycopg',\n",
       " '_range',\n",
       " 'apilevel',\n",
       " 'compat',\n",
       " 'connect',\n",
       " 'errors',\n",
       " 'extensions',\n",
       " 'paramstyle',\n",
       " 'threadsafety',\n",
       " 'tz']"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import psycopg2\n",
    "dir(psycopg2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    }
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Help on function connect in module psycopg2:\n",
      "\n",
      "connect(dsn=None, connection_factory=None, cursor_factory=None, **kwargs)\n",
      "    Create a new database connection.\n",
      "    \n",
      "    The connection parameters can be specified as a string:\n",
      "    \n",
      "        conn = psycopg2.connect(\"dbname=test user=postgres password=secret\")\n",
      "    \n",
      "    or using a set of keyword arguments:\n",
      "    \n",
      "        conn = psycopg2.connect(database=\"test\", user=\"postgres\", password=\"secret\")\n",
      "    \n",
      "    Or as a mix of both. The basic connection parameters are:\n",
      "    \n",
      "    - *dbname*: the database name\n",
      "    - *database*: the database name (only as keyword argument)\n",
      "    - *user*: user name used to authenticate\n",
      "    - *password*: password used to authenticate\n",
      "    - *host*: database host address (defaults to UNIX socket if not provided)\n",
      "    - *port*: connection port number (defaults to 5432 if not provided)\n",
      "    \n",
      "    Using the *connection_factory* parameter a different class or connections\n",
      "    factory can be specified. It should be a callable object taking a dsn\n",
      "    argument.\n",
      "    \n",
      "    Using the *cursor_factory* parameter, a new default cursor factory will be\n",
      "    used by cursor().\n",
      "    \n",
      "    Using *async*=True an asynchronous connection will be created. *async_* is\n",
      "    a valid alias (for Python versions where ``async`` is a keyword).\n",
      "    \n",
      "    Any other keyword parameter will be passed to the underlying client\n",
      "    library: the list of supported parameters depends on the library version.\n",
      "\n"
     ]
    }
   ],
   "source": [
    "help(psycopg2.connect)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "dbname = 'vcnlcpsj'\n",
    "user = 'vcnlcpsj'\n",
    "password = 'wCVuZq-biifESAFhoRpDIlG2r4eD9fgj'\n",
    "host = 'rajje.db.elephantsql.com'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "pg_curs = pg_conn.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "pg_curs.execute('SELECT * FROM test_table;')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(2, 'a second row', {'a': 1, 'b': ['dog', 'cat'], 'c': True})]"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pg_curs.fetchall()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sqlite3\n",
    "sl_conn = sqlite3.connect('rpg_db.sqlite3')\n",
    "sl_curs = sl_conn.cursor()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(302,)]"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sl_curs.execute('SELECT COUNT(*) FROM charactercreator_character').fetchall()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(297,)]"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sl_curs.execute('SELECT COUNT(DISTINCT name) FROM charactercreator_character').fetchall()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "characters = sl_curs.execute('SELECT * from charactercreator_character').fetchall()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 'Aliquid iste optio reiciendi', 0, 0, 10, 1, 1, 1, 1)"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "characters[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(302, 'Aliquam n', 0, 0, 10, 1, 1, 1, 1)"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "characters[-1]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "302"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "len(characters)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(0, 'character_id', 'integer', 1, None, 1),\n",
       " (1, 'name', 'varchar(30)', 1, None, 0),\n",
       " (2, 'level', 'integer', 1, None, 0),\n",
       " (3, 'exp', 'integer', 1, None, 0),\n",
       " (4, 'hp', 'integer', 1, None, 0),\n",
       " (5, 'strength', 'integer', 1, None, 0),\n",
       " (6, 'intelligence', 'integer', 1, None, 0),\n",
       " (7, 'dexterity', 'integer', 1, None, 0),\n",
       " (8, 'wisdom', 'integer', 1, None, 0)]"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sl_curs.execute('PRAGMA table_info(charactercreator_character);').fetchall()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"If you have an invalid SQL statement or typo and you get the current transaction aborted method, \n",
    "close and reopen conn and curs\"\"\"\n",
    "pg_curs.close() #closed the cursor\n",
    "pg_conn.commit() #commited changes to database\n",
    "pg_conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host) #reopened connection\n",
    "pg_curs = pg_conn.cursor() #reopened the cursor"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "create_character_table = \"\"\"\n",
    "  CREATE TABLE charactercreator_character (\n",
    "    character_id SERIAL PRIMARY KEY,\n",
    "    name VARCHAR(30),\n",
    "    level INT,\n",
    "    exp INT,\n",
    "    hp INT,\n",
    "    strength INT,\n",
    "    intelligence INT,\n",
    "    dexterity INT,\n",
    "    wisdom INT\n",
    "  );\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [],
   "source": [
    "pg_curs.execute(create_character_table)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [],
   "source": [
    "show_tables = \"\"\"\n",
    "SELECT *\n",
    "FROM pg_catalog.pg_tables\n",
    "WHERE schemaname != 'pg_catalog'\n",
    "AND schemaname != 'information_schema';\n",
    "\"\"\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[('public', 'test_table', 'vcnlcpsj', None, True, False, False, False),\n",
       " ('public',\n",
       "  'charactercreator_character',\n",
       "  'vcnlcpsj',\n",
       "  None,\n",
       "  True,\n",
       "  False,\n",
       "  False,\n",
       "  False)]"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pg_curs.execute(show_tables)\n",
    "pg_curs.fetchall()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 'Aliquid iste optio reiciendi', 0, 0, 10, 1, 1, 1, 1)"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "characters[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "\"('Aliquid iste optio reiciendi', 0, 0, 10, 1, 1, 1, 1)\""
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "str(characters[0][1:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "INSERT INTO charactercreator_character\n",
      "(name, level, exp, hp, strength, intelligence, dexterity, wisdom)\n",
      "VALUES ('Aliquid iste optio reiciendi', 0, 0, 10, 1, 1, 1, 1);\n"
     ]
    }
   ],
   "source": [
    "example_insert = \"\"\"\n",
    "INSERT INTO charactercreator_character\n",
    "(name, level, exp, hp, strength, intelligence, dexterity, wisdom)\n",
    "VALUES \"\"\" + str(characters[0][1:]) + \";\"\n",
    "\n",
    "print(example_insert)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "for character in characters:\n",
    "  insert_character = \"\"\"\n",
    "    INSERT INTO charactercreator_character\n",
    "    (name, level, exp, hp, strength, intelligence, dexterity, wisdom)\n",
    "    VALUES \"\"\" + str(character[1:]) + \";\"\n",
    "  pg_curs.execute(insert_character)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {
    "collapsed": true,
    "jupyter": {
     "outputs_hidden": true
    }
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(1, 'Aliquid iste optio reiciendi', 0, 0, 10, 1, 1, 1, 1),\n",
       " (2, 'Optio dolorem ex a', 0, 0, 10, 1, 1, 1, 1),\n",
       " (3, 'Minus c', 0, 0, 10, 1, 1, 1, 1),\n",
       " (4, 'Sit ut repr', 0, 0, 10, 1, 1, 1, 1),\n",
       " (5, 'At id recusandae expl', 0, 0, 10, 1, 1, 1, 1),\n",
       " (6, 'Non nobis et of', 0, 0, 10, 1, 1, 1, 1),\n",
       " (7, 'Perferendis', 0, 0, 10, 1, 1, 1, 1),\n",
       " (8, 'Accusantium amet quidem eve', 0, 0, 10, 1, 1, 1, 1),\n",
       " (9, 'Sed nostrum inventore error m', 0, 0, 10, 1, 1, 1, 1),\n",
       " (10, 'Harum repellendus omnis od', 0, 0, 10, 1, 1, 1, 1),\n",
       " (11, 'Itaque ut commodi,', 0, 0, 10, 1, 1, 1, 1),\n",
       " (12, 'Molestiae quis', 0, 0, 10, 1, 1, 1, 1),\n",
       " (13, 'Ali', 0, 0, 10, 1, 1, 1, 1),\n",
       " (14, 'Tempora quod optio possimus il', 0, 0, 10, 1, 1, 1, 1),\n",
       " (15, 'Sed itaque beatae pari', 0, 0, 10, 1, 1, 1, 1),\n",
       " (16, 'Quam dolor', 0, 0, 10, 1, 1, 1, 1),\n",
       " (17, 'Molestias expedita', 0, 0, 10, 1, 1, 1, 1),\n",
       " (18, 'Lauda', 0, 0, 10, 1, 1, 1, 1),\n",
       " (19, 'Incidunt sint perferen', 0, 0, 10, 1, 1, 1, 1),\n",
       " (20, 'Laboriosa', 0, 0, 10, 1, 1, 1, 1),\n",
       " (21, 'Dolore esse nesciunt fugit com', 0, 0, 10, 1, 1, 1, 1),\n",
       " (22, 'Dolorum nam reic', 0, 0, 10, 1, 1, 1, 1),\n",
       " (23, 'Repellat ad numquam volu', 0, 0, 10, 1, 1, 1, 1),\n",
       " (24, 'Facere enim velit eligend', 0, 0, 10, 1, 1, 1, 1),\n",
       " (25, 'Sed ratione quis rep', 0, 0, 10, 1, 1, 1, 1),\n",
       " (26, 'Doloribus neque', 0, 0, 10, 1, 1, 1, 1),\n",
       " (27, 'Ab voluptas se', 0, 0, 10, 1, 1, 1, 1),\n",
       " (28, 'Molestias m', 0, 0, 10, 1, 1, 1, 1),\n",
       " (29, 'In pariatur corpori', 0, 0, 10, 1, 1, 1, 1),\n",
       " (30, 'Possimus ad dignissimos vel, a', 0, 0, 10, 1, 1, 1, 1),\n",
       " (31, 'At minus accusa', 0, 0, 10, 1, 1, 1, 1),\n",
       " (32, 'Ad necess', 0, 0, 10, 1, 1, 1, 1),\n",
       " (33, 'Expedita c', 0, 0, 10, 1, 1, 1, 1),\n",
       " (34, 'Voluptates sunt voluptas volu', 0, 0, 10, 1, 1, 1, 1),\n",
       " (35, 'Autem mollitia fuga lauda', 0, 0, 10, 1, 1, 1, 1),\n",
       " (36, 'Sint quibusdam ob', 0, 0, 10, 1, 1, 1, 1),\n",
       " (37, 'Rerum et o', 0, 0, 10, 1, 1, 1, 1),\n",
       " (38, 'Doloribus dolore r', 0, 0, 10, 1, 1, 1, 1),\n",
       " (39, 'Eaque su', 0, 0, 10, 1, 1, 1, 1),\n",
       " (40, 'Vel molestias numqua', 0, 0, 10, 1, 1, 1, 1),\n",
       " (41, 'Iste assumenda repellat q', 0, 0, 10, 1, 1, 1, 1),\n",
       " (42, 'Animi labo', 0, 0, 10, 1, 1, 1, 1),\n",
       " (43, 'Eum culpa eaque ea omn', 0, 0, 10, 1, 1, 1, 1),\n",
       " (44, 'Harum provident vel quam', 0, 0, 10, 1, 1, 1, 1),\n",
       " (45, 'Aspe', 0, 0, 10, 1, 1, 1, 1),\n",
       " (46, 'Nisi nequ', 0, 0, 10, 1, 1, 1, 1),\n",
       " (47, 'Quod tempora', 0, 0, 10, 1, 1, 1, 1),\n",
       " (48, 'Porro aliq', 0, 0, 10, 1, 1, 1, 1),\n",
       " (49, 'Quas', 0, 0, 10, 1, 1, 1, 1),\n",
       " (50, 'Magnam eligendi quia animi', 0, 0, 10, 1, 1, 1, 1),\n",
       " (51, 'Officiis se', 0, 0, 10, 1, 1, 1, 1),\n",
       " (52, 'Id assumend', 0, 0, 10, 1, 1, 1, 1),\n",
       " (53, 'Voluptatibus fu', 0, 0, 10, 1, 1, 1, 1),\n",
       " (54, 'Odit rat', 0, 0, 10, 1, 1, 1, 1),\n",
       " (55, 'Debit', 0, 0, 10, 1, 1, 1, 1),\n",
       " (56, 'Cum aut quas repudia', 0, 0, 10, 1, 1, 1, 1),\n",
       " (57, 'Deleniti qui quae quidem', 0, 0, 10, 1, 1, 1, 1),\n",
       " (58, 'Adipisci voluptas', 0, 0, 10, 1, 1, 1, 1),\n",
       " (59, 'Debitis sit ratione eos nam', 0, 0, 10, 1, 1, 1, 1),\n",
       " (60, 'Esse illo molestias archi', 0, 0, 10, 1, 1, 1, 1),\n",
       " (61, 'Sunt at itaque voluptatum d', 0, 0, 10, 1, 1, 1, 1),\n",
       " (62, 'Est totam', 0, 0, 10, 1, 1, 1, 1),\n",
       " (63, 'Reprehenderit commodi eius', 0, 0, 10, 1, 1, 1, 1),\n",
       " (64, 'Debit', 0, 0, 10, 1, 1, 1, 1),\n",
       " (65, 'Soluta dol', 0, 0, 10, 1, 1, 1, 1),\n",
       " (66, 'Vel nesc', 0, 0, 10, 1, 1, 1, 1),\n",
       " (67, 'Ratione quia ali', 0, 0, 10, 1, 1, 1, 1),\n",
       " (68, 'Rerum recusandae minima', 0, 0, 10, 1, 1, 1, 1),\n",
       " (69, 'Totam natus eius fugiat volu', 0, 0, 10, 1, 1, 1, 1),\n",
       " (70, 'Perferendis commodi null', 0, 0, 10, 1, 1, 1, 1),\n",
       " (71, 'Laudantiu', 0, 0, 10, 1, 1, 1, 1),\n",
       " (72, 'Voluptat', 0, 0, 10, 1, 1, 1, 1),\n",
       " (73, 'Incidunt nesciun', 0, 0, 10, 1, 1, 1, 1),\n",
       " (74, 'Illum amet vero', 0, 0, 10, 1, 1, 1, 1),\n",
       " (75, 'Suscipit exercitationem re', 0, 0, 10, 1, 1, 1, 1),\n",
       " (76, 'Quas enim error maxime nisi m', 0, 0, 10, 1, 1, 1, 1),\n",
       " (77, 'Labore qu', 0, 0, 10, 1, 1, 1, 1),\n",
       " (78, 'Repudiandae deleniti unde', 0, 0, 10, 1, 1, 1, 1),\n",
       " (79, 'Ut do', 0, 0, 10, 1, 1, 1, 1),\n",
       " (80, 'Quaerat esse labore q', 0, 0, 10, 1, 1, 1, 1),\n",
       " (81, 'Quidem aliq', 0, 0, 10, 1, 1, 1, 1),\n",
       " (82, 'Aperiam vitae eos dolor sed', 0, 0, 10, 1, 1, 1, 1),\n",
       " (83, 'Minus nobis porro', 0, 0, 10, 1, 1, 1, 1),\n",
       " (84, 'In similique', 0, 0, 10, 1, 1, 1, 1),\n",
       " (85, 'Culpa repellat unde', 0, 0, 10, 1, 1, 1, 1),\n",
       " (86, 'Architecto i', 0, 0, 10, 1, 1, 1, 1),\n",
       " (87, 'A sed pariatur qua', 0, 0, 10, 1, 1, 1, 1),\n",
       " (88, 'Tempore assumenda aperiam', 0, 0, 10, 1, 1, 1, 1),\n",
       " (89, 'Sed ullam tempora iusto co', 0, 0, 10, 1, 1, 1, 1),\n",
       " (90, 'Ipsa', 0, 0, 10, 1, 1, 1, 1),\n",
       " (91, 'Fugiat incidun', 0, 0, 10, 1, 1, 1, 1),\n",
       " (92, 'Molestiae of', 0, 0, 10, 1, 1, 1, 1),\n",
       " (93, 'Quae quisquam cons', 0, 0, 10, 1, 1, 1, 1),\n",
       " (94, 'Repellendus ea non facil', 0, 0, 10, 1, 1, 1, 1),\n",
       " (95, 'Quod non quibu', 0, 0, 10, 1, 1, 1, 1),\n",
       " (96, 'Numquam velit distinctio', 0, 0, 10, 1, 1, 1, 1),\n",
       " (97, 'Necessitatibus nihil ex debi', 0, 0, 10, 1, 1, 1, 1),\n",
       " (98, 'Velit tempore nemo, na', 0, 0, 10, 1, 1, 1, 1),\n",
       " (99, 'Nesciunt v', 0, 0, 10, 1, 1, 1, 1),\n",
       " (100, 'Dicta enim debitis accusantiu', 0, 0, 10, 1, 1, 1, 1),\n",
       " (101, 'Vitae a', 0, 0, 10, 1, 1, 1, 1),\n",
       " (102, 'Praesentium voluptas u', 0, 0, 10, 1, 1, 1, 1),\n",
       " (103, 'Unde ullam mollitia? Nu', 0, 0, 10, 1, 1, 1, 1),\n",
       " (104, 'Neque molestias qu', 0, 0, 10, 1, 1, 1, 1),\n",
       " (105, 'Officiis es', 0, 0, 10, 1, 1, 1, 1),\n",
       " (106, 'Beatae mi', 0, 0, 10, 1, 1, 1, 1),\n",
       " (107, 'Mollitia nam corporis temp', 0, 0, 10, 1, 1, 1, 1),\n",
       " (108, 'Repudiandae repellat i', 0, 0, 10, 1, 1, 1, 1),\n",
       " (109, 'Laboriosam', 0, 0, 10, 1, 1, 1, 1),\n",
       " (110, 'Nam minus amet', 0, 0, 10, 1, 1, 1, 1),\n",
       " (111, 'Harum quae volup', 0, 0, 10, 1, 1, 1, 1),\n",
       " (112, 'Impedit facere ulla', 0, 0, 10, 1, 1, 1, 1),\n",
       " (113, 'Enim', 0, 0, 10, 1, 1, 1, 1),\n",
       " (114, 'Dolore magni', 0, 0, 10, 1, 1, 1, 1),\n",
       " (115, 'Eaque at corpori', 0, 0, 10, 1, 1, 1, 1),\n",
       " (116, 'Fug', 0, 0, 10, 1, 1, 1, 1),\n",
       " (117, 'Dolorum laudanti', 0, 0, 10, 1, 1, 1, 1),\n",
       " (118, 'Perferendis nat', 0, 0, 10, 1, 1, 1, 1),\n",
       " (119, 'Cupidi', 0, 0, 10, 1, 1, 1, 1),\n",
       " (120, 'Commodi eius dicta digniss', 0, 0, 10, 1, 1, 1, 1),\n",
       " (121, 'Debitis eu', 0, 0, 10, 1, 1, 1, 1),\n",
       " (122, 'Nihil repella', 0, 0, 10, 1, 1, 1, 1),\n",
       " (123, 'Rem quasi minima hic sed anim', 0, 0, 10, 1, 1, 1, 1),\n",
       " (124, 'Sed ali', 0, 0, 10, 1, 1, 1, 1),\n",
       " (125, 'Earum vol', 0, 0, 10, 1, 1, 1, 1),\n",
       " (126, 'Inventore tempore com', 0, 0, 10, 1, 1, 1, 1),\n",
       " (127, 'Repell', 0, 0, 10, 1, 1, 1, 1),\n",
       " (128, 'Consequatur quis recusandae qu', 0, 0, 10, 1, 1, 1, 1),\n",
       " (129, 'Dolores ea velit mi', 0, 0, 10, 1, 1, 1, 1),\n",
       " (130, 'Atque blanditiis a aperiam', 0, 0, 10, 1, 1, 1, 1),\n",
       " (131, 'Reprehenderit sequi iu', 0, 0, 10, 1, 1, 1, 1),\n",
       " (132, 'Natus architecto eos, hic blan', 0, 0, 10, 1, 1, 1, 1),\n",
       " (133, 'Ipsa illo quas', 0, 0, 10, 1, 1, 1, 1),\n",
       " (134, 'Voluptas ali', 0, 0, 10, 1, 1, 1, 1),\n",
       " (135, 'Voluptates obcaecati quod e', 0, 0, 10, 1, 1, 1, 1),\n",
       " (136, 'Dolor adipisci a voluptate', 0, 0, 10, 1, 1, 1, 1),\n",
       " (137, 'Repellendus natus quae, n', 0, 0, 10, 1, 1, 1, 1),\n",
       " (138, 'Laudantium earum nam in dol', 0, 0, 10, 1, 1, 1, 1),\n",
       " (139, 'Molestias face', 0, 0, 10, 1, 1, 1, 1),\n",
       " (140, 'Maiores suscipit exc', 0, 0, 10, 1, 1, 1, 1),\n",
       " (141, 'Illum dolore perferen', 0, 0, 10, 1, 1, 1, 1),\n",
       " (142, 'Explicabo recusandae ma', 0, 0, 10, 1, 1, 1, 1),\n",
       " (143, 'Odio obcaecati hic nostrum n', 0, 0, 10, 1, 1, 1, 1),\n",
       " (144, 'Voluptate ali', 0, 0, 10, 1, 1, 1, 1),\n",
       " (145, 'Repudiandae vitae sapiente mol', 0, 0, 10, 1, 1, 1, 1),\n",
       " (146, 'Ipsam cumque', 0, 0, 10, 1, 1, 1, 1),\n",
       " (147, 'Fugiat quos alias eos dese', 0, 0, 10, 1, 1, 1, 1),\n",
       " (148, 'Eaque impe', 0, 0, 10, 1, 1, 1, 1),\n",
       " (149, 'Elige', 0, 0, 10, 1, 1, 1, 1),\n",
       " (150, 'Adip', 0, 0, 10, 1, 1, 1, 1),\n",
       " (151, 'Fuga nemo vel mo', 0, 0, 10, 1, 1, 1, 1),\n",
       " (152, 'Libero cumque impedit eveniet', 0, 0, 10, 1, 1, 1, 1),\n",
       " (153, 'Odio soluta', 0, 0, 10, 1, 1, 1, 1),\n",
       " (154, 'Vero nostrum duc', 0, 0, 10, 1, 1, 1, 1),\n",
       " (155, 'Repellend', 0, 0, 10, 1, 1, 1, 1),\n",
       " (156, 'Quod', 0, 0, 10, 1, 1, 1, 1),\n",
       " (157, 'Suscipit reiciend', 0, 0, 10, 1, 1, 1, 1),\n",
       " (158, 'Voluptat', 0, 0, 10, 1, 1, 1, 1),\n",
       " (159, 'Porro dolor fuga quam', 0, 0, 10, 1, 1, 1, 1),\n",
       " (160, 'Amet quo fugit aliquam sequi', 0, 0, 10, 1, 1, 1, 1),\n",
       " (161, 'Magni adipisci veritatis sit q', 0, 0, 10, 1, 1, 1, 1),\n",
       " (162, 'Debitis enim cumque cum qu', 0, 0, 10, 1, 1, 1, 1),\n",
       " (163, 'Dolorem eligend', 0, 0, 10, 1, 1, 1, 1),\n",
       " (164, 'Autem lib', 0, 0, 10, 1, 1, 1, 1),\n",
       " (165, 'Saepe assumenda perferendis f', 0, 0, 10, 1, 1, 1, 1),\n",
       " (166, 'Deserunt', 0, 0, 10, 1, 1, 1, 1),\n",
       " (167, 'Provident soluta simil', 0, 0, 10, 1, 1, 1, 1),\n",
       " (168, 'In accu', 0, 0, 10, 1, 1, 1, 1),\n",
       " (169, 'Inve', 0, 0, 10, 1, 1, 1, 1),\n",
       " (170, 'Placeat sapiente', 0, 0, 10, 1, 1, 1, 1),\n",
       " (171, 'Ducimus architecto ullam', 0, 0, 10, 1, 1, 1, 1),\n",
       " (172, 'Voluptate tempora rerum', 0, 0, 10, 1, 1, 1, 1),\n",
       " (173, 'Totam incidunt earum perspicia', 0, 0, 10, 1, 1, 1, 1),\n",
       " (174, 'Optio quas e', 0, 0, 10, 1, 1, 1, 1),\n",
       " (175, 'Ab illum invento', 0, 0, 10, 1, 1, 1, 1),\n",
       " (176, 'Repellat quis natus totam, s', 0, 0, 10, 1, 1, 1, 1),\n",
       " (177, 'Est voluptate accusantium tem', 0, 0, 10, 1, 1, 1, 1),\n",
       " (178, 'Beatae q', 0, 0, 10, 1, 1, 1, 1),\n",
       " (179, 'Velit', 0, 0, 10, 1, 1, 1, 1),\n",
       " (180, 'Minus nequ', 0, 0, 10, 1, 1, 1, 1),\n",
       " (181, 'Autem eos voluptates off', 0, 0, 10, 1, 1, 1, 1),\n",
       " (182, 'Vel fug', 0, 0, 10, 1, 1, 1, 1),\n",
       " (183, 'Architecto repudian', 0, 0, 10, 1, 1, 1, 1),\n",
       " (184, 'Opti', 0, 0, 10, 1, 1, 1, 1),\n",
       " (185, 'Iust', 0, 0, 10, 1, 1, 1, 1),\n",
       " (186, 'Sapiente', 0, 0, 10, 1, 1, 1, 1),\n",
       " (187, 'Officiis repellat corrupti su', 0, 0, 10, 1, 1, 1, 1),\n",
       " (188, 'Dicta et natus e', 0, 0, 10, 1, 1, 1, 1),\n",
       " (189, 'At quos', 0, 0, 10, 1, 1, 1, 1),\n",
       " (190, 'Laborum ven', 0, 0, 10, 1, 1, 1, 1),\n",
       " (191, 'Exceptur', 0, 0, 10, 1, 1, 1, 1),\n",
       " (192, 'Reiciendis assumenda dolo', 0, 0, 10, 1, 1, 1, 1),\n",
       " (193, 'Poss', 0, 0, 10, 1, 1, 1, 1),\n",
       " (194, 'Acc', 0, 0, 10, 1, 1, 1, 1),\n",
       " (195, 'Placeat esse archit', 0, 0, 10, 1, 1, 1, 1),\n",
       " (196, 'Enim repellendus nihil est te', 0, 0, 10, 1, 1, 1, 1),\n",
       " (197, 'Ipsam incidunt t', 0, 0, 10, 1, 1, 1, 1),\n",
       " (198, 'Iure', 0, 0, 10, 1, 1, 1, 1),\n",
       " (199, 'Illo en', 0, 0, 10, 1, 1, 1, 1),\n",
       " (200, 'A rem ex', 0, 0, 10, 1, 1, 1, 1),\n",
       " (201, 'Officiis su', 0, 0, 10, 1, 1, 1, 1),\n",
       " (202, 'Numquam molestias', 0, 0, 10, 1, 1, 1, 1),\n",
       " (203, 'Voluptates unde', 0, 0, 10, 1, 1, 1, 1),\n",
       " (204, 'Quae praesentium vel', 0, 0, 10, 1, 1, 1, 1),\n",
       " (205, 'Quas', 0, 0, 10, 1, 1, 1, 1),\n",
       " (206, 'Dolores aliquid inv', 0, 0, 10, 1, 1, 1, 1),\n",
       " (207, 'Mollitia tempore laborum eaqu', 0, 0, 10, 1, 1, 1, 1),\n",
       " (208, 'Nobis voluptates fugiat quia', 0, 0, 10, 1, 1, 1, 1),\n",
       " (209, 'Similique dolorem dolore maio', 0, 0, 10, 1, 1, 1, 1),\n",
       " (210, 'Sapiente', 0, 0, 10, 1, 1, 1, 1),\n",
       " (211, 'Officia nisi dolore', 0, 0, 10, 1, 1, 1, 1),\n",
       " (212, 'Distinctio', 0, 0, 10, 1, 1, 1, 1),\n",
       " (213, 'Eos quia dignissimos saepe vel', 0, 0, 10, 1, 1, 1, 1),\n",
       " (214, 'Ullam neque sint eligendi', 0, 0, 10, 1, 1, 1, 1),\n",
       " (215, 'Excepturi deleniti ab a', 0, 0, 10, 1, 1, 1, 1),\n",
       " (216, 'Accusa', 0, 0, 10, 1, 1, 1, 1),\n",
       " (217, 'Reiciendis laboriosam di', 0, 0, 10, 1, 1, 1, 1),\n",
       " (218, 'Delectus ex', 0, 0, 10, 1, 1, 1, 1),\n",
       " (219, 'Pari', 0, 0, 10, 1, 1, 1, 1),\n",
       " (220, 'Veritatis velit facilis iste', 0, 0, 10, 1, 1, 1, 1),\n",
       " (221, 'Dol', 0, 0, 10, 1, 1, 1, 1),\n",
       " (222, 'Qui iste pr', 0, 0, 10, 1, 1, 1, 1),\n",
       " (223, 'Deleni', 0, 0, 10, 1, 1, 1, 1),\n",
       " (224, 'Reprehenderit volu', 0, 0, 10, 1, 1, 1, 1),\n",
       " (225, 'Accusantium vitae n', 0, 0, 10, 1, 1, 1, 1),\n",
       " (226, 'Natus consequatur incidun', 0, 0, 10, 1, 1, 1, 1),\n",
       " (227, 'Dignissimos a', 0, 0, 10, 1, 1, 1, 1),\n",
       " (228, 'Vitae modi', 0, 0, 10, 1, 1, 1, 1),\n",
       " (229, 'Accusantium qu', 0, 0, 10, 1, 1, 1, 1),\n",
       " (230, 'Reiciendis dignissimos ratio', 0, 0, 10, 1, 1, 1, 1),\n",
       " (231, 'Expedita provident natus volup', 0, 0, 10, 1, 1, 1, 1),\n",
       " (232, 'Rerum repellat voluptas c', 0, 0, 10, 1, 1, 1, 1),\n",
       " (233, 'Maiores quos incidunt dolor', 0, 0, 10, 1, 1, 1, 1),\n",
       " (234, 'Aper', 0, 0, 10, 1, 1, 1, 1),\n",
       " (235, 'Nulla', 0, 0, 10, 1, 1, 1, 1),\n",
       " (236, 'Laudantium tempora itaque', 0, 0, 10, 1, 1, 1, 1),\n",
       " (237, 'Reprehenderit', 0, 0, 10, 1, 1, 1, 1),\n",
       " (238, 'Aliqu', 0, 0, 10, 1, 1, 1, 1),\n",
       " (239, 'Odio harum nam mole', 0, 0, 10, 1, 1, 1, 1),\n",
       " (240, 'Arc', 0, 0, 10, 1, 1, 1, 1),\n",
       " (241, 'Reprehenderit li', 0, 0, 10, 1, 1, 1, 1),\n",
       " (242, 'Repr', 0, 0, 10, 1, 1, 1, 1),\n",
       " (243, 'Optio m', 0, 0, 10, 1, 1, 1, 1),\n",
       " (244, 'Esse odit amet rep', 0, 0, 10, 1, 1, 1, 1),\n",
       " (245, 'Provident nostrum minima', 0, 0, 10, 1, 1, 1, 1),\n",
       " (246, 'Ex nihil quae facilis a omni', 0, 0, 10, 1, 1, 1, 1),\n",
       " (247, 'Dolorem quaerat sunt', 0, 0, 10, 1, 1, 1, 1),\n",
       " (248, 'Distinctio', 0, 0, 10, 1, 1, 1, 1),\n",
       " (249, 'Repudiandae ip', 0, 0, 10, 1, 1, 1, 1),\n",
       " (250, 'Iste debitis dolorum amet m', 0, 0, 10, 1, 1, 1, 1),\n",
       " (251, 'Non qui vo', 0, 0, 10, 1, 1, 1, 1),\n",
       " (252, 'Dolorem ma', 0, 0, 10, 1, 1, 1, 1),\n",
       " (253, 'Molestias labore tempore ita', 0, 0, 10, 1, 1, 1, 1),\n",
       " (254, 'Vol', 0, 0, 10, 1, 1, 1, 1),\n",
       " (255, 'Adipisci molest', 0, 0, 10, 1, 1, 1, 1),\n",
       " (256, 'Omni', 0, 0, 10, 1, 1, 1, 1),\n",
       " (257, 'Voluptatibus dolor', 0, 0, 10, 1, 1, 1, 1),\n",
       " (258, 'Quo', 0, 0, 10, 1, 1, 1, 1),\n",
       " (259, 'Atque aspernatur possi', 0, 0, 10, 1, 1, 1, 1),\n",
       " (260, 'Ullam c', 0, 0, 10, 1, 1, 1, 1),\n",
       " (261, 'Iusto quas voluptatibu', 0, 0, 10, 1, 1, 1, 1),\n",
       " (262, 'Optio qui sunt dolores, ab', 0, 0, 10, 1, 1, 1, 1),\n",
       " (263, 'Illum recusandae nulla re', 0, 0, 10, 1, 1, 1, 1),\n",
       " (264, 'Verita', 0, 0, 10, 1, 1, 1, 1),\n",
       " (265, 'Expedita quod blanditiis', 0, 0, 10, 1, 1, 1, 1),\n",
       " (266, 'Mag', 0, 0, 10, 1, 1, 1, 1),\n",
       " (267, 'Omnis quos aspernatur d', 0, 0, 10, 1, 1, 1, 1),\n",
       " (268, 'Sunt impedit co', 0, 0, 10, 1, 1, 1, 1),\n",
       " (269, 'Minima quam ea ad', 0, 0, 10, 1, 1, 1, 1),\n",
       " (270, 'Suscipit quidem e', 0, 0, 10, 1, 1, 1, 1),\n",
       " (271, 'Harum', 0, 0, 10, 1, 1, 1, 1),\n",
       " (272, 'Dolore laborum ips', 0, 0, 10, 1, 1, 1, 1),\n",
       " (273, 'Magni veniam earum corporis', 0, 0, 10, 1, 1, 1, 1),\n",
       " (274, 'Optio', 0, 0, 10, 1, 1, 1, 1),\n",
       " (275, 'Nam fugit vel.', 0, 0, 10, 1, 1, 1, 1),\n",
       " (276, 'Ut numquam quam eum, alias ius', 0, 0, 10, 1, 1, 1, 1),\n",
       " (277, 'Error amet tempore nulla', 0, 0, 10, 1, 1, 1, 1),\n",
       " (278, 'Deserunt a', 0, 0, 10, 1, 1, 1, 1),\n",
       " (279, 'Aperiam sit', 0, 0, 10, 1, 1, 1, 1),\n",
       " (280, 'Asperi', 0, 0, 10, 1, 1, 1, 1),\n",
       " (281, 'Similique aperiam earum expli', 0, 0, 10, 1, 1, 1, 1),\n",
       " (282, 'Iure h', 0, 0, 10, 1, 1, 1, 1),\n",
       " (283, 'At sint ducimus nostrum i', 0, 0, 10, 1, 1, 1, 1),\n",
       " (284, 'Reprehenderit temporib', 0, 0, 10, 1, 1, 1, 1),\n",
       " (285, 'Molestiae quaerat maxim', 0, 0, 10, 1, 1, 1, 1),\n",
       " (286, 'Maior', 0, 0, 10, 1, 1, 1, 1),\n",
       " (287, 'Unde natus ut ipsa cupi', 0, 0, 10, 1, 1, 1, 1),\n",
       " (288, 'Praesentium atque ear', 0, 0, 10, 1, 1, 1, 1),\n",
       " (289, 'Rem minima', 0, 0, 10, 1, 1, 1, 1),\n",
       " (290, 'Provident sed soluta, sed si', 0, 0, 10, 1, 1, 1, 1),\n",
       " (291, 'Natus quia veritatis', 0, 0, 10, 1, 1, 1, 1),\n",
       " (292, 'Vero a', 0, 0, 10, 1, 1, 1, 1),\n",
       " (293, 'Optio harum labori', 0, 0, 10, 1, 1, 1, 1),\n",
       " (294, 'Duci', 0, 0, 10, 1, 1, 1, 1),\n",
       " (295, 'Ipsa elige', 0, 0, 10, 1, 1, 1, 1),\n",
       " (296, 'Sunt blanditiis i', 0, 0, 10, 1, 1, 1, 1),\n",
       " (297, 'Doloremque', 0, 0, 10, 1, 1, 1, 1),\n",
       " (298, 'Autem ratione vitae quos, do', 0, 0, 10, 1, 1, 1, 1),\n",
       " (299, 'Voluptatibus aliquid', 0, 0, 10, 1, 1, 1, 1),\n",
       " (300, 'Quaerat sequi sit eius corpori', 0, 0, 10, 1, 1, 1, 1),\n",
       " (301, 'Libe', 0, 0, 10, 1, 1, 1, 1),\n",
       " (302, 'Aliquam n', 0, 0, 10, 1, 1, 1, 1)]"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pg_curs.execute('SELECT * from charactercreator_character;')\n",
    "pg_curs.fetchall()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "pg_curs.close()\n",
    "pg_conn.commit()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "pg_curs = pg_conn.cursor()\n",
    "pg_curs.execute('SELECT * FROM charactercreator_character;')\n",
    "pg_characters = pg_curs.fetchall()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(1, 'Aliquid iste optio reiciendi', 0, 0, 10, 1, 1, 1, 1),\n",
       " (2, 'Optio dolorem ex a', 0, 0, 10, 1, 1, 1, 1),\n",
       " (3, 'Minus c', 0, 0, 10, 1, 1, 1, 1)]"
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "characters[0:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[(1, 'Aliquid iste optio reiciendi', 0, 0, 10, 1, 1, 1, 1),\n",
       " (2, 'Optio dolorem ex a', 0, 0, 10, 1, 1, 1, 1),\n",
       " (3, 'Minus c', 0, 0, 10, 1, 1, 1, 1)]"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pg_characters[0:3]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [],
   "source": [
    "for character, pg_character in zip(characters, pg_characters):\n",
    "  assert character == pg_character"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
