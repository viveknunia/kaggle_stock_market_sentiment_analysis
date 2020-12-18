{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "kaggle_stock_sent_analysis.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "metadata": {
        "id": "el4z3cNKv1gC"
      },
      "source": [
        "import pandas as pd"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "jsGtLKoYv-Pf"
      },
      "source": [
        "df = pd.read_csv('https://raw.githubusercontent.com/krishnaik06/Stock-Sentiment-Analysis/master/Data.csv',encoding = 'ISO-8859-1')"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 753
        },
        "id": "gXDZRcxawBjH",
        "outputId": "6f203e25-056c-4d5f-9759-64c9dfa06293"
      },
      "source": [
        "df.head()"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>Date</th>\n",
              "      <th>Label</th>\n",
              "      <th>Top1</th>\n",
              "      <th>Top2</th>\n",
              "      <th>Top3</th>\n",
              "      <th>Top4</th>\n",
              "      <th>Top5</th>\n",
              "      <th>Top6</th>\n",
              "      <th>Top7</th>\n",
              "      <th>Top8</th>\n",
              "      <th>Top9</th>\n",
              "      <th>Top10</th>\n",
              "      <th>Top11</th>\n",
              "      <th>Top12</th>\n",
              "      <th>Top13</th>\n",
              "      <th>Top14</th>\n",
              "      <th>Top15</th>\n",
              "      <th>Top16</th>\n",
              "      <th>Top17</th>\n",
              "      <th>Top18</th>\n",
              "      <th>Top19</th>\n",
              "      <th>Top20</th>\n",
              "      <th>Top21</th>\n",
              "      <th>Top22</th>\n",
              "      <th>Top23</th>\n",
              "      <th>Top24</th>\n",
              "      <th>Top25</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>2000-01-03</td>\n",
              "      <td>0</td>\n",
              "      <td>A 'hindrance to operations': extracts from the...</td>\n",
              "      <td>Scorecard</td>\n",
              "      <td>Hughes' instant hit buoys Blues</td>\n",
              "      <td>Jack gets his skates on at ice-cold Alex</td>\n",
              "      <td>Chaos as Maracana builds up for United</td>\n",
              "      <td>Depleted Leicester prevail as Elliott spoils E...</td>\n",
              "      <td>Hungry Spurs sense rich pickings</td>\n",
              "      <td>Gunners so wide of an easy target</td>\n",
              "      <td>Derby raise a glass to Strupar's debut double</td>\n",
              "      <td>Southgate strikes, Leeds pay the penalty</td>\n",
              "      <td>Hammers hand Robson a youthful lesson</td>\n",
              "      <td>Saints party like it's 1999</td>\n",
              "      <td>Wear wolves have turned into lambs</td>\n",
              "      <td>Stump mike catches testy Gough's taunt</td>\n",
              "      <td>Langer escapes to hit 167</td>\n",
              "      <td>Flintoff injury piles on woe for England</td>\n",
              "      <td>Hunters threaten Jospin with new battle of the...</td>\n",
              "      <td>Kohl's successor drawn into scandal</td>\n",
              "      <td>The difference between men and women</td>\n",
              "      <td>Sara Denver, nurse turned solicitor</td>\n",
              "      <td>Diana's landmine crusade put Tories in a panic</td>\n",
              "      <td>Yeltsin's resignation caught opposition flat-f...</td>\n",
              "      <td>Russian roulette</td>\n",
              "      <td>Sold out</td>\n",
              "      <td>Recovering a title</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>2000-01-04</td>\n",
              "      <td>0</td>\n",
              "      <td>Scorecard</td>\n",
              "      <td>The best lake scene</td>\n",
              "      <td>Leader: German sleaze inquiry</td>\n",
              "      <td>Cheerio, boyo</td>\n",
              "      <td>The main recommendations</td>\n",
              "      <td>Has Cubie killed fees?</td>\n",
              "      <td>Has Cubie killed fees?</td>\n",
              "      <td>Has Cubie killed fees?</td>\n",
              "      <td>Hopkins 'furious' at Foster's lack of Hannibal...</td>\n",
              "      <td>Has Cubie killed fees?</td>\n",
              "      <td>A tale of two tails</td>\n",
              "      <td>I say what I like and I like what I say</td>\n",
              "      <td>Elbows, Eyes and Nipples</td>\n",
              "      <td>Task force to assess risk of asteroid collision</td>\n",
              "      <td>How I found myself at last</td>\n",
              "      <td>On the critical list</td>\n",
              "      <td>The timing of their lives</td>\n",
              "      <td>Dear doctor</td>\n",
              "      <td>Irish court halts IRA man's extradition to Nor...</td>\n",
              "      <td>Burundi peace initiative fades after rebels re...</td>\n",
              "      <td>PE points the way forward to the ECB</td>\n",
              "      <td>Campaigners keep up pressure on Nazi war crime...</td>\n",
              "      <td>Jane Ratcliffe</td>\n",
              "      <td>Yet more things you wouldn't know without the ...</td>\n",
              "      <td>Millennium bug fails to bite</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>2000-01-05</td>\n",
              "      <td>0</td>\n",
              "      <td>Coventry caught on counter by Flo</td>\n",
              "      <td>United's rivals on the road to Rio</td>\n",
              "      <td>Thatcher issues defence before trial by video</td>\n",
              "      <td>Police help Smith lay down the law at Everton</td>\n",
              "      <td>Tale of Trautmann bears two more retellings</td>\n",
              "      <td>England on the rack</td>\n",
              "      <td>Pakistan retaliate with call for video of Walsh</td>\n",
              "      <td>Cullinan continues his Cape monopoly</td>\n",
              "      <td>McGrath puts India out of their misery</td>\n",
              "      <td>Blair Witch bandwagon rolls on</td>\n",
              "      <td>Pele turns up heat on Ferguson</td>\n",
              "      <td>Party divided over Kohl slush fund scandal</td>\n",
              "      <td>Manchester United (England)</td>\n",
              "      <td>Women in record South Pole walk</td>\n",
              "      <td>Vasco da Gama (Brazil)</td>\n",
              "      <td>South Melbourne (Australia)</td>\n",
              "      <td>Necaxa (Mexico)</td>\n",
              "      <td>Real Madrid (Spain)</td>\n",
              "      <td>Raja Casablanca (Morocco)</td>\n",
              "      <td>Corinthians (Brazil)</td>\n",
              "      <td>Tony's pet project</td>\n",
              "      <td>Al Nassr (Saudi Arabia)</td>\n",
              "      <td>Ideal Holmes show</td>\n",
              "      <td>Pinochet leaves hospital after tests</td>\n",
              "      <td>Useful links</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>2000-01-06</td>\n",
              "      <td>1</td>\n",
              "      <td>Pilgrim knows how to progress</td>\n",
              "      <td>Thatcher facing ban</td>\n",
              "      <td>McIlroy calls for Irish fighting spirit</td>\n",
              "      <td>Leicester bin stadium blueprint</td>\n",
              "      <td>United braced for Mexican wave</td>\n",
              "      <td>Auntie back in fashion, even if the dress look...</td>\n",
              "      <td>Shoaib appeal goes to the top</td>\n",
              "      <td>Hussain hurt by 'shambles' but lays blame on e...</td>\n",
              "      <td>England's decade of disasters</td>\n",
              "      <td>Revenge is sweet for jubilant Cronje</td>\n",
              "      <td>Our choice, not theirs</td>\n",
              "      <td>Profile of former US Nazi Party officer Willia...</td>\n",
              "      <td>New evidence shows record of war crimes suspec...</td>\n",
              "      <td>The rise of the supernerds</td>\n",
              "      <td>Written on the body</td>\n",
              "      <td>Putin admits Yeltsin quit to give him a head s...</td>\n",
              "      <td>BBC worst hit as digital TV begins to bite</td>\n",
              "      <td>How much can you pay for...</td>\n",
              "      <td>Christmas glitches</td>\n",
              "      <td>Upending a table, Chopping a line and Scoring ...</td>\n",
              "      <td>Scientific evidence 'unreliable', defence claims</td>\n",
              "      <td>Fusco wins judicial review in extradition case</td>\n",
              "      <td>Rebels thwart Russian advance</td>\n",
              "      <td>Blair orders shake-up of failing NHS</td>\n",
              "      <td>Lessons of law's hard heart</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>2000-01-07</td>\n",
              "      <td>1</td>\n",
              "      <td>Hitches and Horlocks</td>\n",
              "      <td>Beckham off but United survive</td>\n",
              "      <td>Breast cancer screening</td>\n",
              "      <td>Alan Parker</td>\n",
              "      <td>Guardian readers: are you all whingers?</td>\n",
              "      <td>Hollywood Beyond</td>\n",
              "      <td>Ashes and diamonds</td>\n",
              "      <td>Whingers - a formidable minority</td>\n",
              "      <td>Alan Parker - part two</td>\n",
              "      <td>Thuggery, Toxins and Ties</td>\n",
              "      <td>Met faces fresh attack on race crime</td>\n",
              "      <td>Everton fans top racist 'league of shame'</td>\n",
              "      <td>Our breasts, ourselves</td>\n",
              "      <td>Russia's new boss has an extremely strange his...</td>\n",
              "      <td>Always and forever</td>\n",
              "      <td>Most everywhere:  UDIs</td>\n",
              "      <td>Most wanted:  Chloe lunettes</td>\n",
              "      <td>Return of the cane 'completely off the agenda'</td>\n",
              "      <td>From Sleepy Hollow to Greeneland</td>\n",
              "      <td>Blunkett outlines vision for over 11s</td>\n",
              "      <td>Embattled Dobson attacks 'play now, pay later'...</td>\n",
              "      <td>Doom and the Dome</td>\n",
              "      <td>What is the north-south divide?</td>\n",
              "      <td>Aitken released from jail</td>\n",
              "      <td>Gone aloft</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "         Date  ...                         Top25\n",
              "0  2000-01-03  ...            Recovering a title\n",
              "1  2000-01-04  ...  Millennium bug fails to bite\n",
              "2  2000-01-05  ...                  Useful links\n",
              "3  2000-01-06  ...   Lessons of law's hard heart\n",
              "4  2000-01-07  ...                    Gone aloft\n",
              "\n",
              "[5 rows x 27 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 5
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "rNysYXMzwO8U"
      },
      "source": [
        "train = df[df['Date'] < '20150101']\r\n",
        "test = df[df['Date'] > '20141231']"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 753
        },
        "id": "vrP8QjW1wpiI",
        "outputId": "b49c9ade-3f11-4c2f-cd47-fd77150998a6"
      },
      "source": [
        "data = train.iloc[:,2:27]\r\n",
        "data.replace('[^a-zA-Z]',' ',regex = True,inplace = True)\r\n",
        "list1 =[i for i in range(25)]\r\n",
        "new_index=[str(i) for i in list1]\r\n",
        "data.columns = new_index\r\n",
        "data.head(5)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>0</th>\n",
              "      <th>1</th>\n",
              "      <th>2</th>\n",
              "      <th>3</th>\n",
              "      <th>4</th>\n",
              "      <th>5</th>\n",
              "      <th>6</th>\n",
              "      <th>7</th>\n",
              "      <th>8</th>\n",
              "      <th>9</th>\n",
              "      <th>10</th>\n",
              "      <th>11</th>\n",
              "      <th>12</th>\n",
              "      <th>13</th>\n",
              "      <th>14</th>\n",
              "      <th>15</th>\n",
              "      <th>16</th>\n",
              "      <th>17</th>\n",
              "      <th>18</th>\n",
              "      <th>19</th>\n",
              "      <th>20</th>\n",
              "      <th>21</th>\n",
              "      <th>22</th>\n",
              "      <th>23</th>\n",
              "      <th>24</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>A  hindrance to operations   extracts from the...</td>\n",
              "      <td>Scorecard</td>\n",
              "      <td>Hughes  instant hit buoys Blues</td>\n",
              "      <td>Jack gets his skates on at ice cold Alex</td>\n",
              "      <td>Chaos as Maracana builds up for United</td>\n",
              "      <td>Depleted Leicester prevail as Elliott spoils E...</td>\n",
              "      <td>Hungry Spurs sense rich pickings</td>\n",
              "      <td>Gunners so wide of an easy target</td>\n",
              "      <td>Derby raise a glass to Strupar s debut double</td>\n",
              "      <td>Southgate strikes  Leeds pay the penalty</td>\n",
              "      <td>Hammers hand Robson a youthful lesson</td>\n",
              "      <td>Saints party like it s</td>\n",
              "      <td>Wear wolves have turned into lambs</td>\n",
              "      <td>Stump mike catches testy Gough s taunt</td>\n",
              "      <td>Langer escapes to hit</td>\n",
              "      <td>Flintoff injury piles on woe for England</td>\n",
              "      <td>Hunters threaten Jospin with new battle of the...</td>\n",
              "      <td>Kohl s successor drawn into scandal</td>\n",
              "      <td>The difference between men and women</td>\n",
              "      <td>Sara Denver  nurse turned solicitor</td>\n",
              "      <td>Diana s landmine crusade put Tories in a panic</td>\n",
              "      <td>Yeltsin s resignation caught opposition flat f...</td>\n",
              "      <td>Russian roulette</td>\n",
              "      <td>Sold out</td>\n",
              "      <td>Recovering a title</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>1</th>\n",
              "      <td>Scorecard</td>\n",
              "      <td>The best lake scene</td>\n",
              "      <td>Leader  German sleaze inquiry</td>\n",
              "      <td>Cheerio  boyo</td>\n",
              "      <td>The main recommendations</td>\n",
              "      <td>Has Cubie killed fees</td>\n",
              "      <td>Has Cubie killed fees</td>\n",
              "      <td>Has Cubie killed fees</td>\n",
              "      <td>Hopkins  furious  at Foster s lack of Hannibal...</td>\n",
              "      <td>Has Cubie killed fees</td>\n",
              "      <td>A tale of two tails</td>\n",
              "      <td>I say what I like and I like what I say</td>\n",
              "      <td>Elbows  Eyes and Nipples</td>\n",
              "      <td>Task force to assess risk of asteroid collision</td>\n",
              "      <td>How I found myself at last</td>\n",
              "      <td>On the critical list</td>\n",
              "      <td>The timing of their lives</td>\n",
              "      <td>Dear doctor</td>\n",
              "      <td>Irish court halts IRA man s extradition to Nor...</td>\n",
              "      <td>Burundi peace initiative fades after rebels re...</td>\n",
              "      <td>PE points the way forward to the ECB</td>\n",
              "      <td>Campaigners keep up pressure on Nazi war crime...</td>\n",
              "      <td>Jane Ratcliffe</td>\n",
              "      <td>Yet more things you wouldn t know without the ...</td>\n",
              "      <td>Millennium bug fails to bite</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>2</th>\n",
              "      <td>Coventry caught on counter by Flo</td>\n",
              "      <td>United s rivals on the road to Rio</td>\n",
              "      <td>Thatcher issues defence before trial by video</td>\n",
              "      <td>Police help Smith lay down the law at Everton</td>\n",
              "      <td>Tale of Trautmann bears two more retellings</td>\n",
              "      <td>England on the rack</td>\n",
              "      <td>Pakistan retaliate with call for video of Walsh</td>\n",
              "      <td>Cullinan continues his Cape monopoly</td>\n",
              "      <td>McGrath puts India out of their misery</td>\n",
              "      <td>Blair Witch bandwagon rolls on</td>\n",
              "      <td>Pele turns up heat on Ferguson</td>\n",
              "      <td>Party divided over Kohl slush fund scandal</td>\n",
              "      <td>Manchester United  England</td>\n",
              "      <td>Women in record South Pole walk</td>\n",
              "      <td>Vasco da Gama  Brazil</td>\n",
              "      <td>South Melbourne  Australia</td>\n",
              "      <td>Necaxa  Mexico</td>\n",
              "      <td>Real Madrid  Spain</td>\n",
              "      <td>Raja Casablanca  Morocco</td>\n",
              "      <td>Corinthians  Brazil</td>\n",
              "      <td>Tony s pet project</td>\n",
              "      <td>Al Nassr  Saudi Arabia</td>\n",
              "      <td>Ideal Holmes show</td>\n",
              "      <td>Pinochet leaves hospital after tests</td>\n",
              "      <td>Useful links</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>3</th>\n",
              "      <td>Pilgrim knows how to progress</td>\n",
              "      <td>Thatcher facing ban</td>\n",
              "      <td>McIlroy calls for Irish fighting spirit</td>\n",
              "      <td>Leicester bin stadium blueprint</td>\n",
              "      <td>United braced for Mexican wave</td>\n",
              "      <td>Auntie back in fashion  even if the dress look...</td>\n",
              "      <td>Shoaib appeal goes to the top</td>\n",
              "      <td>Hussain hurt by  shambles  but lays blame on e...</td>\n",
              "      <td>England s decade of disasters</td>\n",
              "      <td>Revenge is sweet for jubilant Cronje</td>\n",
              "      <td>Our choice  not theirs</td>\n",
              "      <td>Profile of former US Nazi Party officer Willia...</td>\n",
              "      <td>New evidence shows record of war crimes suspec...</td>\n",
              "      <td>The rise of the supernerds</td>\n",
              "      <td>Written on the body</td>\n",
              "      <td>Putin admits Yeltsin quit to give him a head s...</td>\n",
              "      <td>BBC worst hit as digital TV begins to bite</td>\n",
              "      <td>How much can you pay for</td>\n",
              "      <td>Christmas glitches</td>\n",
              "      <td>Upending a table  Chopping a line and Scoring ...</td>\n",
              "      <td>Scientific evidence  unreliable   defence claims</td>\n",
              "      <td>Fusco wins judicial review in extradition case</td>\n",
              "      <td>Rebels thwart Russian advance</td>\n",
              "      <td>Blair orders shake up of failing NHS</td>\n",
              "      <td>Lessons of law s hard heart</td>\n",
              "    </tr>\n",
              "    <tr>\n",
              "      <th>4</th>\n",
              "      <td>Hitches and Horlocks</td>\n",
              "      <td>Beckham off but United survive</td>\n",
              "      <td>Breast cancer screening</td>\n",
              "      <td>Alan Parker</td>\n",
              "      <td>Guardian readers  are you all whingers</td>\n",
              "      <td>Hollywood Beyond</td>\n",
              "      <td>Ashes and diamonds</td>\n",
              "      <td>Whingers   a formidable minority</td>\n",
              "      <td>Alan Parker   part two</td>\n",
              "      <td>Thuggery  Toxins and Ties</td>\n",
              "      <td>Met faces fresh attack on race crime</td>\n",
              "      <td>Everton fans top racist  league of shame</td>\n",
              "      <td>Our breasts  ourselves</td>\n",
              "      <td>Russia s new boss has an extremely strange his...</td>\n",
              "      <td>Always and forever</td>\n",
              "      <td>Most everywhere   UDIs</td>\n",
              "      <td>Most wanted   Chloe lunettes</td>\n",
              "      <td>Return of the cane  completely off the agenda</td>\n",
              "      <td>From Sleepy Hollow to Greeneland</td>\n",
              "      <td>Blunkett outlines vision for over   s</td>\n",
              "      <td>Embattled Dobson attacks  play now  pay later ...</td>\n",
              "      <td>Doom and the Dome</td>\n",
              "      <td>What is the north south divide</td>\n",
              "      <td>Aitken released from jail</td>\n",
              "      <td>Gone aloft</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                                                   0  ...                            24\n",
              "0  A  hindrance to operations   extracts from the...  ...            Recovering a title\n",
              "1                                          Scorecard  ...  Millennium bug fails to bite\n",
              "2                  Coventry caught on counter by Flo  ...                  Useful links\n",
              "3                      Pilgrim knows how to progress  ...   Lessons of law s hard heart\n",
              "4                               Hitches and Horlocks  ...                    Gone aloft\n",
              "\n",
              "[5 rows x 25 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 27
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 214
        },
        "id": "6Hw6_SQPxAlD",
        "outputId": "e345e099-f911-4aaf-edd9-3908f8fe4d06"
      },
      "source": [
        "for index in new_index:\r\n",
        "    data[index] = data[index].str.lower()\r\n",
        "data.head(1)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/html": [
              "<div>\n",
              "<style scoped>\n",
              "    .dataframe tbody tr th:only-of-type {\n",
              "        vertical-align: middle;\n",
              "    }\n",
              "\n",
              "    .dataframe tbody tr th {\n",
              "        vertical-align: top;\n",
              "    }\n",
              "\n",
              "    .dataframe thead th {\n",
              "        text-align: right;\n",
              "    }\n",
              "</style>\n",
              "<table border=\"1\" class=\"dataframe\">\n",
              "  <thead>\n",
              "    <tr style=\"text-align: right;\">\n",
              "      <th></th>\n",
              "      <th>0</th>\n",
              "      <th>1</th>\n",
              "      <th>2</th>\n",
              "      <th>3</th>\n",
              "      <th>4</th>\n",
              "      <th>5</th>\n",
              "      <th>6</th>\n",
              "      <th>7</th>\n",
              "      <th>8</th>\n",
              "      <th>9</th>\n",
              "      <th>10</th>\n",
              "      <th>11</th>\n",
              "      <th>12</th>\n",
              "      <th>13</th>\n",
              "      <th>14</th>\n",
              "      <th>15</th>\n",
              "      <th>16</th>\n",
              "      <th>17</th>\n",
              "      <th>18</th>\n",
              "      <th>19</th>\n",
              "      <th>20</th>\n",
              "      <th>21</th>\n",
              "      <th>22</th>\n",
              "      <th>23</th>\n",
              "      <th>24</th>\n",
              "    </tr>\n",
              "  </thead>\n",
              "  <tbody>\n",
              "    <tr>\n",
              "      <th>0</th>\n",
              "      <td>a  hindrance to operations   extracts from the...</td>\n",
              "      <td>scorecard</td>\n",
              "      <td>hughes  instant hit buoys blues</td>\n",
              "      <td>jack gets his skates on at ice cold alex</td>\n",
              "      <td>chaos as maracana builds up for united</td>\n",
              "      <td>depleted leicester prevail as elliott spoils e...</td>\n",
              "      <td>hungry spurs sense rich pickings</td>\n",
              "      <td>gunners so wide of an easy target</td>\n",
              "      <td>derby raise a glass to strupar s debut double</td>\n",
              "      <td>southgate strikes  leeds pay the penalty</td>\n",
              "      <td>hammers hand robson a youthful lesson</td>\n",
              "      <td>saints party like it s</td>\n",
              "      <td>wear wolves have turned into lambs</td>\n",
              "      <td>stump mike catches testy gough s taunt</td>\n",
              "      <td>langer escapes to hit</td>\n",
              "      <td>flintoff injury piles on woe for england</td>\n",
              "      <td>hunters threaten jospin with new battle of the...</td>\n",
              "      <td>kohl s successor drawn into scandal</td>\n",
              "      <td>the difference between men and women</td>\n",
              "      <td>sara denver  nurse turned solicitor</td>\n",
              "      <td>diana s landmine crusade put tories in a panic</td>\n",
              "      <td>yeltsin s resignation caught opposition flat f...</td>\n",
              "      <td>russian roulette</td>\n",
              "      <td>sold out</td>\n",
              "      <td>recovering a title</td>\n",
              "    </tr>\n",
              "  </tbody>\n",
              "</table>\n",
              "</div>"
            ],
            "text/plain": [
              "                                                   0  ...                  24\n",
              "0  a  hindrance to operations   extracts from the...  ...  recovering a title\n",
              "\n",
              "[1 rows x 25 columns]"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 28
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "37CRSBHTyAar"
      },
      "source": [
        "headlines = []\r\n",
        "for row in range(0,len(data.index)):\r\n",
        "    headlines.append(' '.join(str(x) for x in data.iloc[row,0:25]))"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "8fJuabqQyp28"
      },
      "source": [
        "from sklearn.feature_extraction.text import CountVectorizer\r\n",
        "from sklearn.ensemble import RandomForestClassifier"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "wKo7aD8XzltC"
      },
      "source": [
        "countvector = CountVectorizer(ngram_range = (2,2))\r\n",
        "traindataset = countvector.fit_transform(headlines)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WNUvwPEzzXIO",
        "outputId": "3ed7f53a-0700-4bbc-8272-9baaf677cadc"
      },
      "source": [
        "randomclassifier = RandomForestClassifier(n_estimators=200,criterion='entropy')\r\n",
        "randomclassifier.fit(traindataset,train['Label'])"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "RandomForestClassifier(bootstrap=True, ccp_alpha=0.0, class_weight=None,\n",
              "                       criterion='entropy', max_depth=None, max_features='auto',\n",
              "                       max_leaf_nodes=None, max_samples=None,\n",
              "                       min_impurity_decrease=0.0, min_impurity_split=None,\n",
              "                       min_samples_leaf=1, min_samples_split=2,\n",
              "                       min_weight_fraction_leaf=0.0, n_estimators=200,\n",
              "                       n_jobs=None, oob_score=False, random_state=None,\n",
              "                       verbose=0, warm_start=False)"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 32
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "JzyZNRohz8Qc"
      },
      "source": [
        "test_transform = []\r\n",
        "for i in range(0,len(test.index)):\r\n",
        "    test_transform.append(' '.join(str(x) for x in test.iloc[i,2:27]))\r\n",
        "test_dataset = countvector.transform(test_transform)\r\n",
        "predictions = randomclassifier.predict(test_dataset)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "afXhj-z70kML"
      },
      "source": [
        "from sklearn.metrics import classification_report,confusion_matrix,accuracy_score"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "WvqLMmsM0ycS",
        "outputId": "0efc3c8c-cad8-4c8d-bb81-efb2a3f0a75c"
      },
      "source": [
        "matrix = confusion_matrix(test['Label'],predictions)\r\n",
        "print(matrix)\r\n",
        "accuracy = accuracy_score(test['Label'],predictions)\r\n",
        "print(accuracy)\r\n",
        "report =  classification_report(test['Label'],predictions)\r\n",
        "print(report)"
      ],
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "[[136  50]\n",
            " [  7 185]]\n",
            "0.8492063492063492\n",
            "              precision    recall  f1-score   support\n",
            "\n",
            "           0       0.95      0.73      0.83       186\n",
            "           1       0.79      0.96      0.87       192\n",
            "\n",
            "    accuracy                           0.85       378\n",
            "   macro avg       0.87      0.85      0.85       378\n",
            "weighted avg       0.87      0.85      0.85       378\n",
            "\n"
          ],
          "name": "stdout"
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "fe6VYDy9069D"
      },
      "source": [
        ""
      ],
      "execution_count": null,
      "outputs": []
    }
  ]
}