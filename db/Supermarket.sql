PGDMP         
        	        {            Supermarket    15.2    15.2 "               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16769    Supermarket    DATABASE     �   CREATE DATABASE "Supermarket" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE "Supermarket";
                postgres    false            �            1259    16863    sm_employees    TABLE     �   CREATE TABLE public.sm_employees (
    id integer NOT NULL,
    name text,
    age integer,
    phone text,
    hire_date date,
    salary numeric,
    functionid integer,
    shiftid integer
);
     DROP TABLE public.sm_employees;
       public         heap    postgres    false            �            1259    16862    employees_employeeid_seq    SEQUENCE     �   CREATE SEQUENCE public.employees_employeeid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.employees_employeeid_seq;
       public          postgres    false    219                       0    0    employees_employeeid_seq    SEQUENCE OWNED BY     P   ALTER SEQUENCE public.employees_employeeid_seq OWNED BY public.sm_employees.id;
          public          postgres    false    218            �            1259    16776    sm_functions    TABLE     s   CREATE TABLE public.sm_functions (
    id integer NOT NULL,
    name text,
    workload text,
    location text
);
     DROP TABLE public.sm_functions;
       public         heap    postgres    false            �            1259    16775    functions_functionid_seq    SEQUENCE     �   CREATE SEQUENCE public.functions_functionid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.functions_functionid_seq;
       public          postgres    false    215                       0    0    functions_functionid_seq    SEQUENCE OWNED BY     P   ALTER SEQUENCE public.functions_functionid_seq OWNED BY public.sm_functions.id;
          public          postgres    false    214            �            1259    16856 	   sm_shifts    TABLE     }   CREATE TABLE public.sm_shifts (
    id integer NOT NULL,
    start date,
    hour integer,
    workhours double precision
);
    DROP TABLE public.sm_shifts;
       public         heap    postgres    false            �            1259    16855    shifts_shiftid_seq    SEQUENCE     �   CREATE SEQUENCE public.shifts_shiftid_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 )   DROP SEQUENCE public.shifts_shiftid_seq;
       public          postgres    false    217                        0    0    shifts_shiftid_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.shifts_shiftid_seq OWNED BY public.sm_shifts.id;
          public          postgres    false    216            �            1259    17073    sm_inventory    TABLE     �   CREATE TABLE public.sm_inventory (
    id integer NOT NULL,
    item text,
    quantity double precision,
    entry_date date,
    exp_date date,
    kosher boolean
);
     DROP TABLE public.sm_inventory;
       public         heap    postgres    false            �            1259    17072    storage_id_seq    SEQUENCE     �   CREATE SEQUENCE public.storage_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.storage_id_seq;
       public          postgres    false    221            !           0    0    storage_id_seq    SEQUENCE OWNED BY     F   ALTER SEQUENCE public.storage_id_seq OWNED BY public.sm_inventory.id;
          public          postgres    false    220            v           2604    16866    sm_employees id    DEFAULT     w   ALTER TABLE ONLY public.sm_employees ALTER COLUMN id SET DEFAULT nextval('public.employees_employeeid_seq'::regclass);
 >   ALTER TABLE public.sm_employees ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    218    219            t           2604    16779    sm_functions id    DEFAULT     w   ALTER TABLE ONLY public.sm_functions ALTER COLUMN id SET DEFAULT nextval('public.functions_functionid_seq'::regclass);
 >   ALTER TABLE public.sm_functions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    214    215            w           2604    17076    sm_inventory id    DEFAULT     m   ALTER TABLE ONLY public.sm_inventory ALTER COLUMN id SET DEFAULT nextval('public.storage_id_seq'::regclass);
 >   ALTER TABLE public.sm_inventory ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    221    220    221            u           2604    16859    sm_shifts id    DEFAULT     n   ALTER TABLE ONLY public.sm_shifts ALTER COLUMN id SET DEFAULT nextval('public.shifts_shiftid_seq'::regclass);
 ;   ALTER TABLE public.sm_shifts ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    216    217    217                      0    16863    sm_employees 
   TABLE DATA           d   COPY public.sm_employees (id, name, age, phone, hire_date, salary, functionid, shiftid) FROM stdin;
    public          postgres    false    219   e%                 0    16776    sm_functions 
   TABLE DATA           D   COPY public.sm_functions (id, name, workload, location) FROM stdin;
    public          postgres    false    215   �%                 0    17073    sm_inventory 
   TABLE DATA           X   COPY public.sm_inventory (id, item, quantity, entry_date, exp_date, kosher) FROM stdin;
    public          postgres    false    221   9&                 0    16856 	   sm_shifts 
   TABLE DATA           ?   COPY public.sm_shifts (id, start, hour, workhours) FROM stdin;
    public          postgres    false    217   �&       "           0    0    employees_employeeid_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.employees_employeeid_seq', 3, true);
          public          postgres    false    218            #           0    0    functions_functionid_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.functions_functionid_seq', 4, true);
          public          postgres    false    214            $           0    0    shifts_shiftid_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.shifts_shiftid_seq', 4, true);
          public          postgres    false    216            %           0    0    storage_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.storage_id_seq', 5, true);
          public          postgres    false    220            }           2606    16870    sm_employees employees_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.sm_employees
    ADD CONSTRAINT employees_pkey PRIMARY KEY (id);
 E   ALTER TABLE ONLY public.sm_employees DROP CONSTRAINT employees_pkey;
       public            postgres    false    219            y           2606    16783    sm_functions functions_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.sm_functions
    ADD CONSTRAINT functions_pkey PRIMARY KEY (id);
 E   ALTER TABLE ONLY public.sm_functions DROP CONSTRAINT functions_pkey;
       public            postgres    false    215            {           2606    16861    sm_shifts shifts_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.sm_shifts
    ADD CONSTRAINT shifts_pkey PRIMARY KEY (id);
 ?   ALTER TABLE ONLY public.sm_shifts DROP CONSTRAINT shifts_pkey;
       public            postgres    false    217                       2606    17080    sm_inventory storage_pkey 
   CONSTRAINT     W   ALTER TABLE ONLY public.sm_inventory
    ADD CONSTRAINT storage_pkey PRIMARY KEY (id);
 C   ALTER TABLE ONLY public.sm_inventory DROP CONSTRAINT storage_pkey;
       public            postgres    false    221            �           2606    16871 &   sm_employees employees_functionid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.sm_employees
    ADD CONSTRAINT employees_functionid_fkey FOREIGN KEY (functionid) REFERENCES public.sm_functions(id);
 P   ALTER TABLE ONLY public.sm_employees DROP CONSTRAINT employees_functionid_fkey;
       public          postgres    false    3193    219    215            �           2606    16876 #   sm_employees employees_shiftid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.sm_employees
    ADD CONSTRAINT employees_shiftid_fkey FOREIGN KEY (shiftid) REFERENCES public.sm_shifts(id);
 M   ALTER TABLE ONLY public.sm_employees DROP CONSTRAINT employees_shiftid_fkey;
       public          postgres    false    217    219    3195               g   x�e˫
�`����*�����dD�������D�`��U�]��+k��{��J��8�!2�4vm��;�$S�
#�z��rm�W�׳�}��O�犈n�~         M   x�3�LN,��L-���L�(�L�HM��/-�2�L�IM�Jd�&�Ur&��ps��'g��2�sR��L�D�<�=... ���         y   x�U�K�0Eѱ��n �8){�$Dn��(r�Ո���=:fGL���k�52<Ud��e���
-�;ȯ1��*�[�_F]�~��l�g�Lf<�����#n��-�[D�"'*�         1   x�3�4202�50"N3N.#dC#��1��9�9�	���	P$F��� �f�     