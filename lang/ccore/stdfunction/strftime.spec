%[ ���η� ] ���η�

===

strftime()ת�����η�

ת�����η�        �ṹ��Ա         �������

a                 tm_wday           �ܼ������� (��д)

A                 tm_wday           �ܼ������� (����)

b��h              tm_mon            �·ݵ����� (��д)

B                 tm_mon            �·ݵ����� (����)

c                 (ȫ��)            ���ں�ʱ��

D                 tm_mon��tm_mday��  %m/%d/%y����д
                  tm_year

d                 tm_mday           ���µĵڼ��죬ʮ���ơ����
                                    С��0����ǰ���һ���ո�ֵ
                                    �ķ�ΧΪ1~31

F                 tm_mon��tm_mday�� %Y-%m-%d����д
                  tm_year

g                 tm_year��tm_wday��ISO 8601 "���ܼ��������" �����
                  tm_yday           �����������֡���ΧΪ00~99

G                 tm_year��tm_wday��ISO 8601 "���ܼ��������" �����
                  tm_yday           ��ֵ (�ĸ�����)

H                 tm_hour           ��ʮ��Сʱ�Ƶ� "ʱ"����ΧΪ00~23

I                 tm_hour           ��ʮ��Сʱ�Ƶ� "ʱ"��ʹ���������֣���ΧΪ01~12

j                 tm_yday           һ���еĵڼ��죬ʹ������ʮ��������ʾ����ΧΪ
                                    001~366

m                 tm_mon            �·ݣ�ʹ������ʮ��������ʾ����ΧΪ00~59

n                 (û��)            �����ַ� ('\n')

p                 tm_hour           12Сʱ���У���AM��PM

r                 tm_hour��tm_min�� ʮ��Сʱ�Ƶ�ʱ��
                  tm_sec

R                 tm_hour��tm_min   %H:%M����д

S                 tm_sec            �÷��ӵĵڼ��룬ʹ������ʮ��������ʾ����ΧΪ
                                    00~60

t                 (û��)            �Ʊ��� ('\t')

T                 tm_hour��tm_min   %H:%M:%S����д
                  tm_sec

u                 tm_wday           һ�ܵĵڼ��죬ʹ��һ��ʮ��������ʾ����ΧΪ
                                    1~7������1��ʾ��һ

U                 tm_year��tm_wday  ����ĵڼ��ܣ�ʹ������ʮ��������ʾ����ΧΪ
                  tm_yday           00~53�����е�һ���Ǵ�һ�µĵ�һ������

V                 tm_year��tm_wday  ISO 8601 "���ܼ��������" �еĵڼ��ܣ�ʹ��
                  tm_yday           ����ʮ����λ���� (01~53) ��ʾ����һ�ܴ�һ��
                                    4�յ��ܵ�����һ��ʼ

w                 tm_wday           һ�ܵĵڼ��죬ʹ��һ��ʮ��������ʾ����ΧΪ
                                    0~6������0��������

W                 tm_year��tm_wday��һ��ĵڼ��ܣ�ʹ������ʮ��������ʾ����ΧΪ
                  tm_yday           00~53�����е�һ���Ǵ�һ�µĵ�һ����һ��ʼ��
                                    ���

x                 (ȫ��)            ����

X                 (ȫ��)            ʱ��

y                 tm_year           ��ݵ�����������֣���Χ��00~99

Y                 tm_year           ��Ԫ��� (����: 2005)

z                 tm_isdst          �͸������α�׼ʱ�� (GMT) ��ƫ������֪��
                                    �Ļ������ǿյ� (��Χ��+0200��ʾλ��GMT����
                                    ��Сʱ)

Z                 tm_isdst          ʱ������д�������֪���Ļ������ǿ�

%                 (û��)            �ٷֱȷ��� (%)
