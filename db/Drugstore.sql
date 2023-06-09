PGDMP     )            	        {         	   Drugstore    15.2    15.2 $               0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                        1262    16562 	   Drugstore    DATABASE     �   CREATE DATABASE "Drugstore" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE "Drugstore";
                postgres    false            �            1259    17502    ds_customers    TABLE     �   CREATE TABLE public.ds_customers (
    id integer NOT NULL,
    name text,
    age integer,
    address text,
    phone text
);
     DROP TABLE public.ds_customers;
       public         heap    postgres    false            �            1259    17501    customers_id_seq    SEQUENCE     �   CREATE SEQUENCE public.customers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.customers_id_seq;
       public          postgres    false    215            !           0    0    customers_id_seq    SEQUENCE OWNED BY     H   ALTER SEQUENCE public.customers_id_seq OWNED BY public.ds_customers.id;
          public          postgres    false    214            �            1259    17551    ds_prescriptions    TABLE     �   CREATE TABLE public.ds_prescriptions (
    id integer NOT NULL,
    customerid integer,
    item text,
    quantity integer,
    date date
);
 $   DROP TABLE public.ds_prescriptions;
       public         heap    postgres    false            �            1259    17535 
   ds_storage    TABLE     �   CREATE TABLE public.ds_storage (
    id integer NOT NULL,
    item text,
    quantity integer,
    exp_date date,
    supplierid integer
);
    DROP TABLE public.ds_storage;
       public         heap    postgres    false            �            1259    17511    ds_suppliers    TABLE     m   CREATE TABLE public.ds_suppliers (
    id integer NOT NULL,
    name text,
    phone text,
    email text
);
     DROP TABLE public.ds_suppliers;
       public         heap    postgres    false            �            1259    17550    prescriptions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.prescriptions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 +   DROP SEQUENCE public.prescriptions_id_seq;
       public          postgres    false    221            "           0    0    prescriptions_id_seq    SEQUENCE OWNED BY     P   ALTER SEQUENCE public.prescriptions_id_seq OWNED BY public.ds_prescriptions.id;
          public          postgres    false    220            �            1259    17534    storage_id_seq    SEQUENCE     �   CREATE SEQUENCE public.storage_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.storage_id_seq;
       public          postgres    false    219            #           0    0    storage_id_seq    SEQUENCE OWNED BY     D   ALTER SEQUENCE public.storage_id_seq OWNED BY public.ds_storage.id;
          public          postgres    false    218            �            1259    17510    suppliers_id_seq    SEQUENCE     �   CREATE SEQUENCE public.suppliers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.suppliers_id_seq;
       public          postgres    false    217            $           0    0    suppliers_id_seq    SEQUENCE OWNED BY     H   ALTER SEQUENCE public.suppliers_id_seq OWNED BY public.ds_suppliers.id;
          public          postgres    false    216            t           2604    17505    ds_customers id    DEFAULT     o   ALTER TABLE ONLY public.ds_customers ALTER COLUMN id SET DEFAULT nextval('public.customers_id_seq'::regclass);
 >   ALTER TABLE public.ds_customers ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    215    215            w           2604    17554    ds_prescriptions id    DEFAULT     w   ALTER TABLE ONLY public.ds_prescriptions ALTER COLUMN id SET DEFAULT nextval('public.prescriptions_id_seq'::regclass);
 B   ALTER TABLE public.ds_prescriptions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    221    220    221            v           2604    17538    ds_storage id    DEFAULT     k   ALTER TABLE ONLY public.ds_storage ALTER COLUMN id SET DEFAULT nextval('public.storage_id_seq'::regclass);
 <   ALTER TABLE public.ds_storage ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    218    219            u           2604    17514    ds_suppliers id    DEFAULT     o   ALTER TABLE ONLY public.ds_suppliers ALTER COLUMN id SET DEFAULT nextval('public.suppliers_id_seq'::regclass);
 >   ALTER TABLE public.ds_suppliers ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    216    217                      0    17502    ds_customers 
   TABLE DATA           E   COPY public.ds_customers (id, name, age, address, phone) FROM stdin;
    public          postgres    false    215   �'                 0    17551    ds_prescriptions 
   TABLE DATA           P   COPY public.ds_prescriptions (id, customerid, item, quantity, date) FROM stdin;
    public          postgres    false    221   �(                 0    17535 
   ds_storage 
   TABLE DATA           N   COPY public.ds_storage (id, item, quantity, exp_date, supplierid) FROM stdin;
    public          postgres    false    219   �(                 0    17511    ds_suppliers 
   TABLE DATA           >   COPY public.ds_suppliers (id, name, phone, email) FROM stdin;
    public          postgres    false    217   �(       %           0    0    customers_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.customers_id_seq', 6, true);
          public          postgres    false    214            &           0    0    prescriptions_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.prescriptions_id_seq', 1, false);
          public          postgres    false    220            '           0    0    storage_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.storage_id_seq', 1, false);
          public          postgres    false    218            (           0    0    suppliers_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.suppliers_id_seq', 1, false);
          public          postgres    false    216            y           2606    17509    ds_customers customers_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.ds_customers
    ADD CONSTRAINT customers_pkey PRIMARY KEY (id);
 E   ALTER TABLE ONLY public.ds_customers DROP CONSTRAINT customers_pkey;
       public            postgres    false    215            �           2606    17558 #   ds_prescriptions prescriptions_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public.ds_prescriptions
    ADD CONSTRAINT prescriptions_pkey PRIMARY KEY (id);
 M   ALTER TABLE ONLY public.ds_prescriptions DROP CONSTRAINT prescriptions_pkey;
       public            postgres    false    221            }           2606    17544    ds_storage storage_name_key 
   CONSTRAINT     V   ALTER TABLE ONLY public.ds_storage
    ADD CONSTRAINT storage_name_key UNIQUE (item);
 E   ALTER TABLE ONLY public.ds_storage DROP CONSTRAINT storage_name_key;
       public            postgres    false    219                       2606    17542    ds_storage storage_pkey 
   CONSTRAINT     U   ALTER TABLE ONLY public.ds_storage
    ADD CONSTRAINT storage_pkey PRIMARY KEY (id);
 A   ALTER TABLE ONLY public.ds_storage DROP CONSTRAINT storage_pkey;
       public            postgres    false    219            {           2606    17518    ds_suppliers suppliers_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.ds_suppliers
    ADD CONSTRAINT suppliers_pkey PRIMARY KEY (id);
 E   ALTER TABLE ONLY public.ds_suppliers DROP CONSTRAINT suppliers_pkey;
       public            postgres    false    217            �           2606    17559 .   ds_prescriptions prescriptions_customerid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.ds_prescriptions
    ADD CONSTRAINT prescriptions_customerid_fkey FOREIGN KEY (customerid) REFERENCES public.ds_customers(id);
 X   ALTER TABLE ONLY public.ds_prescriptions DROP CONSTRAINT prescriptions_customerid_fkey;
       public          postgres    false    221    3193    215            �           2606    17564 (   ds_prescriptions prescriptions_name_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.ds_prescriptions
    ADD CONSTRAINT prescriptions_name_fkey FOREIGN KEY (item) REFERENCES public.ds_storage(item);
 R   ALTER TABLE ONLY public.ds_prescriptions DROP CONSTRAINT prescriptions_name_fkey;
       public          postgres    false    219    221    3197            �           2606    17545 "   ds_storage storage_supplierid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.ds_storage
    ADD CONSTRAINT storage_supplierid_fkey FOREIGN KEY (supplierid) REFERENCES public.ds_suppliers(id);
 L   ALTER TABLE ONLY public.ds_storage DROP CONSTRAINT storage_supplierid_fkey;
       public          postgres    false    3195    219    217               �   x�%��n�0������ %v&�eS�"[6F�c#Q����r�O���x	��
#(�僛��"�l]Pn��[����ܕ?�:#���,�x��O��i;^���9ά+JC��5�kaM��Sn���i��r��o���ʛ�^yf���ة�/�$� +�چ?ut�Wify��iIDoN�7�            x������ � �            x������ � �            x������ � �     