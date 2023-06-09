PGDMP         	        	        {            Gym    15.2    15.2                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16832    Gym    DATABASE     |   CREATE DATABASE "Gym" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE "Gym";
                postgres    false            �            1259    17716    gy_customers    TABLE     �   CREATE TABLE public.gy_customers (
    id integer NOT NULL,
    name text,
    age integer,
    membership_start date,
    membership_end date
);
     DROP TABLE public.gy_customers;
       public         heap    postgres    false            �            1259    17715    customers_id_seq    SEQUENCE     �   CREATE SEQUENCE public.customers_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.customers_id_seq;
       public          postgres    false    215                       0    0    customers_id_seq    SEQUENCE OWNED BY     H   ALTER SEQUENCE public.customers_id_seq OWNED BY public.gy_customers.id;
          public          postgres    false    214            �            1259    17725 	   gy_shifts    TABLE     t   CREATE TABLE public.gy_shifts (
    id integer NOT NULL,
    start date,
    hour integer,
    workhours integer
);
    DROP TABLE public.gy_shifts;
       public         heap    postgres    false            �            1259    17732    gy_staff    TABLE     �   CREATE TABLE public.gy_staff (
    id integer NOT NULL,
    name text,
    age integer,
    hire_date date,
    salary numeric,
    shiftid integer
);
    DROP TABLE public.gy_staff;
       public         heap    postgres    false            �            1259    17724    shifts_id_seq    SEQUENCE     �   CREATE SEQUENCE public.shifts_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.shifts_id_seq;
       public          postgres    false    217                       0    0    shifts_id_seq    SEQUENCE OWNED BY     B   ALTER SEQUENCE public.shifts_id_seq OWNED BY public.gy_shifts.id;
          public          postgres    false    216            �            1259    17731    staff_id_seq    SEQUENCE     �   CREATE SEQUENCE public.staff_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 #   DROP SEQUENCE public.staff_id_seq;
       public          postgres    false    219                       0    0    staff_id_seq    SEQUENCE OWNED BY     @   ALTER SEQUENCE public.staff_id_seq OWNED BY public.gy_staff.id;
          public          postgres    false    218            o           2604    17719    gy_customers id    DEFAULT     o   ALTER TABLE ONLY public.gy_customers ALTER COLUMN id SET DEFAULT nextval('public.customers_id_seq'::regclass);
 >   ALTER TABLE public.gy_customers ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    215    215            p           2604    17728    gy_shifts id    DEFAULT     i   ALTER TABLE ONLY public.gy_shifts ALTER COLUMN id SET DEFAULT nextval('public.shifts_id_seq'::regclass);
 ;   ALTER TABLE public.gy_shifts ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    216    217            q           2604    17735    gy_staff id    DEFAULT     g   ALTER TABLE ONLY public.gy_staff ALTER COLUMN id SET DEFAULT nextval('public.staff_id_seq'::regclass);
 :   ALTER TABLE public.gy_staff ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    218    219    219                      0    17716    gy_customers 
   TABLE DATA           W   COPY public.gy_customers (id, name, age, membership_start, membership_end) FROM stdin;
    public          postgres    false    215   �       
          0    17725 	   gy_shifts 
   TABLE DATA           ?   COPY public.gy_shifts (id, start, hour, workhours) FROM stdin;
    public          postgres    false    217   �                 0    17732    gy_staff 
   TABLE DATA           M   COPY public.gy_staff (id, name, age, hire_date, salary, shiftid) FROM stdin;
    public          postgres    false    219   �                  0    0    customers_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.customers_id_seq', 7, true);
          public          postgres    false    214                       0    0    shifts_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.shifts_id_seq', 1, false);
          public          postgres    false    216                       0    0    staff_id_seq    SEQUENCE SET     ;   SELECT pg_catalog.setval('public.staff_id_seq', 1, false);
          public          postgres    false    218            s           2606    17723    gy_customers customers_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.gy_customers
    ADD CONSTRAINT customers_pkey PRIMARY KEY (id);
 E   ALTER TABLE ONLY public.gy_customers DROP CONSTRAINT customers_pkey;
       public            postgres    false    215            u           2606    17730    gy_shifts shifts_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.gy_shifts
    ADD CONSTRAINT shifts_pkey PRIMARY KEY (id);
 ?   ALTER TABLE ONLY public.gy_shifts DROP CONSTRAINT shifts_pkey;
       public            postgres    false    217            w           2606    17739    gy_staff staff_pkey 
   CONSTRAINT     Q   ALTER TABLE ONLY public.gy_staff
    ADD CONSTRAINT staff_pkey PRIMARY KEY (id);
 =   ALTER TABLE ONLY public.gy_staff DROP CONSTRAINT staff_pkey;
       public            postgres    false    219            x           2606    17740    gy_staff staff_shiftid_fkey    FK CONSTRAINT     ~   ALTER TABLE ONLY public.gy_staff
    ADD CONSTRAINT staff_shiftid_fkey FOREIGN KEY (shiftid) REFERENCES public.gy_shifts(id);
 E   ALTER TABLE ONLY public.gy_staff DROP CONSTRAINT staff_shiftid_fkey;
       public          postgres    false    217    219    3189               �   x�E�A
�0EדS��d��vݺ�������l��	�f�?�|��"������B�4�S� �F-$s� �3�$�ͼ_<��%B��U�ͮ&Lܜ�Wk�R��F�-�p���Mཱིɇ��ʩ�;�9�����+Py�d}��z'���_| ��we���� T;�      
      x������ � �            x������ � �     