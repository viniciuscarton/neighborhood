PGDMP                 	        {            Bank    15.2    15.2                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            	           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            
           1262    16452    Bank    DATABASE     }   CREATE DATABASE "Bank" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE "Bank";
                postgres    false            �            1259    17486    ba_accounts    TABLE     {   CREATE TABLE public.ba_accounts (
    id integer NOT NULL,
    number text,
    balance numeric,
    customerid integer
);
    DROP TABLE public.ba_accounts;
       public         heap    postgres    false            �            1259    17485    account_id_seq    SEQUENCE     �   CREATE SEQUENCE public.account_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 %   DROP SEQUENCE public.account_id_seq;
       public          postgres    false    217                       0    0    account_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.account_id_seq OWNED BY public.ba_accounts.id;
          public          postgres    false    216            �            1259    17313    ba_customers    TABLE     p   CREATE TABLE public.ba_customers (
    id integer NOT NULL,
    name text,
    age integer,
    address text
);
     DROP TABLE public.ba_customers;
       public         heap    postgres    false            �            1259    17312    customer_id_seq    SEQUENCE     �   CREATE SEQUENCE public.customer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 &   DROP SEQUENCE public.customer_id_seq;
       public          postgres    false    215                       0    0    customer_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.customer_id_seq OWNED BY public.ba_customers.id;
          public          postgres    false    214            k           2604    17489    ba_accounts id    DEFAULT     l   ALTER TABLE ONLY public.ba_accounts ALTER COLUMN id SET DEFAULT nextval('public.account_id_seq'::regclass);
 =   ALTER TABLE public.ba_accounts ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    216    217    217            j           2604    17316    ba_customers id    DEFAULT     n   ALTER TABLE ONLY public.ba_customers ALTER COLUMN id SET DEFAULT nextval('public.customer_id_seq'::regclass);
 >   ALTER TABLE public.ba_customers ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    215    214    215                      0    17486    ba_accounts 
   TABLE DATA           F   COPY public.ba_accounts (id, number, balance, customerid) FROM stdin;
    public          postgres    false    217   �                 0    17313    ba_customers 
   TABLE DATA           >   COPY public.ba_customers (id, name, age, address) FROM stdin;
    public          postgres    false    215   3                  0    0    account_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.account_id_seq', 7, true);
          public          postgres    false    216                       0    0    customer_id_seq    SEQUENCE SET     =   SELECT pg_catalog.setval('public.customer_id_seq', 7, true);
          public          postgres    false    214            o           2606    17495    ba_accounts account_number_key 
   CONSTRAINT     [   ALTER TABLE ONLY public.ba_accounts
    ADD CONSTRAINT account_number_key UNIQUE (number);
 H   ALTER TABLE ONLY public.ba_accounts DROP CONSTRAINT account_number_key;
       public            postgres    false    217            q           2606    17493    ba_accounts account_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.ba_accounts
    ADD CONSTRAINT account_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.ba_accounts DROP CONSTRAINT account_pkey;
       public            postgres    false    217            m           2606    17320    ba_customers customer_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.ba_customers
    ADD CONSTRAINT customer_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.ba_customers DROP CONSTRAINT customer_pkey;
       public            postgres    false    215            r           2606    17496 #   ba_accounts account_customerid_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.ba_accounts
    ADD CONSTRAINT account_customerid_fkey FOREIGN KEY (customerid) REFERENCES public.ba_customers(id);
 M   ALTER TABLE ONLY public.ba_accounts DROP CONSTRAINT account_customerid_fkey;
       public          postgres    false    3181    217    215               O   x�=���0�3َ?�.������j�#�*"���h4n��>>�t�m�?u�L�����X���,�/���         �   x�%��
�0����)�9I�v)��us���^��}~S��h��a;h6$-Խ��,��u]d���A�<�	�n�4͛�h?Spú$�S�[�����Q9K״čW8���4��C�%��!�V������N)��(7     