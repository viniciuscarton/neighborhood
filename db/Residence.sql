PGDMP                  
        {         	   Residence    15.2    15.2                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    16700 	   Residence    DATABASE     �   CREATE DATABASE "Residence" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Portuguese_Brazil.1252';
    DROP DATABASE "Residence";
                postgres    false            �            1259    17122    re_apartments    TABLE     �   CREATE TABLE public.re_apartments (
    id integer NOT NULL,
    building_name text,
    address text,
    apartment_number integer,
    number_of_rooms integer,
    area integer,
    monthly_rent numeric,
    occupied boolean
);
 !   DROP TABLE public.re_apartments;
       public         heap    postgres    false            �            1259    17121    apartments_id_seq    SEQUENCE     �   CREATE SEQUENCE public.apartments_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.apartments_id_seq;
       public          postgres    false    219                       0    0    apartments_id_seq    SEQUENCE OWNED BY     J   ALTER SEQUENCE public.apartments_id_seq OWNED BY public.re_apartments.id;
          public          postgres    false    218            �            1259    17113 	   re_houses    TABLE     �   CREATE TABLE public.re_houses (
    id integer NOT NULL,
    address text,
    number_of_rooms integer,
    area integer,
    monthly_rent numeric,
    occupied boolean
);
    DROP TABLE public.re_houses;
       public         heap    postgres    false            �            1259    17112    houses_id_seq    SEQUENCE     �   CREATE SEQUENCE public.houses_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 $   DROP SEQUENCE public.houses_id_seq;
       public          postgres    false    217                       0    0    houses_id_seq    SEQUENCE OWNED BY     B   ALTER SEQUENCE public.houses_id_seq OWNED BY public.re_houses.id;
          public          postgres    false    216            �            1259    17083    re_residents    TABLE     �   CREATE TABLE public.re_residents (
    id integer NOT NULL,
    first_name text,
    family_name text,
    email text,
    phone text,
    age integer,
    sex text,
    occupation text,
    religion text,
    property_type text,
    propertyid text
);
     DROP TABLE public.re_residents;
       public         heap    postgres    false            �            1259    17082    residents_resident_id_seq    SEQUENCE     �   CREATE SEQUENCE public.residents_resident_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.residents_resident_id_seq;
       public          postgres    false    215                       0    0    residents_resident_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.residents_resident_id_seq OWNED BY public.re_residents.id;
          public          postgres    false    214            q           2604    17125    re_apartments id    DEFAULT     q   ALTER TABLE ONLY public.re_apartments ALTER COLUMN id SET DEFAULT nextval('public.apartments_id_seq'::regclass);
 ?   ALTER TABLE public.re_apartments ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    218    219    219            p           2604    17116    re_houses id    DEFAULT     i   ALTER TABLE ONLY public.re_houses ALTER COLUMN id SET DEFAULT nextval('public.houses_id_seq'::regclass);
 ;   ALTER TABLE public.re_houses ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    216    217    217            o           2604    17086    re_residents id    DEFAULT     x   ALTER TABLE ONLY public.re_residents ALTER COLUMN id SET DEFAULT nextval('public.residents_resident_id_seq'::regclass);
 >   ALTER TABLE public.re_residents ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    215    215                      0    17122    re_apartments 
   TABLE DATA           �   COPY public.re_apartments (id, building_name, address, apartment_number, number_of_rooms, area, monthly_rent, occupied) FROM stdin;
    public          postgres    false    219   �       	          0    17113 	   re_houses 
   TABLE DATA           _   COPY public.re_houses (id, address, number_of_rooms, area, monthly_rent, occupied) FROM stdin;
    public          postgres    false    217   �                 0    17083    re_residents 
   TABLE DATA           �   COPY public.re_residents (id, first_name, family_name, email, phone, age, sex, occupation, religion, property_type, propertyid) FROM stdin;
    public          postgres    false    215   �                  0    0    apartments_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.apartments_id_seq', 10, true);
          public          postgres    false    218                       0    0    houses_id_seq    SEQUENCE SET     <   SELECT pg_catalog.setval('public.houses_id_seq', 10, true);
          public          postgres    false    216                       0    0    residents_resident_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.residents_resident_id_seq', 14, true);
          public          postgres    false    214            w           2606    17129    re_apartments apartments_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.re_apartments
    ADD CONSTRAINT apartments_pkey PRIMARY KEY (id);
 G   ALTER TABLE ONLY public.re_apartments DROP CONSTRAINT apartments_pkey;
       public            postgres    false    219            u           2606    17120    re_houses houses_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public.re_houses
    ADD CONSTRAINT houses_pkey PRIMARY KEY (id);
 ?   ALTER TABLE ONLY public.re_houses DROP CONSTRAINT houses_pkey;
       public            postgres    false    217            s           2606    17090    re_residents residents_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public.re_residents
    ADD CONSTRAINT residents_pkey PRIMARY KEY (id);
 E   ALTER TABLE ONLY public.re_residents DROP CONSTRAINT residents_pkey;
       public            postgres    false    215                 x�eP�j�0>+O�'��8α�����N���[CӤ8��=�$�º������#x;Fl�����&�#�.@`��R��Y
mH'|�㊻KH�9���t��k��3��L1Y�����*_��pm��D{Zx	�u���ʤH!����DXg|	M��!uqd�!	._�d�Z�>���)�˝�%�2��+��L��)v!�>M�xGr�p�1��`${�L��ا���&�<�I��yٛ�bk�V�R����V-�J�o&����w_w�4�[]��"5|EQ� �C      	   �   x�5��
�0Eד��/�ܼ�.U\��n�V,�EJ���Im��p���y>���ׅ<�ZKN��8
1q���9��X��*�|�"�؊�ea���@IS��H��q��+NO��\h"n��Ӥ�J�/�"$$>v�v�����fQ ���i�{Բ��[Y�FAk�����:ʴ���vƘ��;         �  x�m�˒�0E׭����,?v@�TB�,�T�&����(K�ߧ�]��U���{��ږVV��Us�W֧J=�m��(I�f���l���zZ�OUٓj�K�h�4�_��m�J��Q�G0�q$�4B.��ldsT^���Fy@�wW�'��Z�pX�lk�K�ٝ��c%i!�A���U�/�Z��Ԯ���aQ齺n��>����>B ���/�lT˶(�������W��S�Ƌ�KG����!Q���/ՠ��d��Z���!�_�Au_ŝ%�D#Je]+��� ���#�d�#
���;��~o[�%�}ӺJ�[�'��F���a�/��Y����	�M%}���7F�������A(�w��X�p����"��l�����;��୽���
�x[��Ӽ����X�>k�6�v��`��a+Y²�g.̻��4Ǵ)z����2B��Q]srP�rr�Zq���F�!��('��	!� ��H-     