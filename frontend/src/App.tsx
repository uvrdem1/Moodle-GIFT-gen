import { useState } from 'react'
import axios from 'axios'

function App() {

  const [topic, setTopic] = useState('')

  const [questionsCount, setQuestionsCount] = useState(5)

  const [giftResult, setGiftResult] = useState('')

  const [loading, setLoading] = useState(false)

  const [provider, setProvider] = useState('gigachat')

  const [language, setLanguage] = useState('ru')

  const [questionType, setQuestionType] = useState('single')

  const [answersCount, setAnswersCount] = useState(4)

  const [sourceText, setSourceText] = useState('')


  const generateQuestions = async () => {

    try {

      setLoading(true)

      const response = await axios.post(
        'http://127.0.0.1:8000/api/generate/',
        {
          topic,
          questions_count: questionsCount,
          provider,
          language,
          question_type: questionType,
          answers_count: answersCount,
          source_text: sourceText,
        }
      )

      setGiftResult(response.data.gift)

    } catch (error) {

      console.error(error)

      alert('Ошибка генерации вопросов')

    } finally {

      setLoading(false)
    }
  }


  const downloadGift = () => {

    const blob = new Blob(
      [giftResult],
      { type: 'text/plain' }
    )

    const url = window.URL.createObjectURL(blob)

    const a = document.createElement('a')

    a.href = url

    a.download = 'questions.gift'

    a.click()

    window.URL.revokeObjectURL(url)
  }


  const copyGift = async () => {

    await navigator.clipboard.writeText(
      giftResult
    )

    alert('GIFT скопирован')
  }


  return (
    <div className="min-h-screen bg-gray-100 p-10">

      <div className="max-w-7xl mx-auto bg-white rounded-2xl shadow-xl p-10">

        <h1 className="text-5xl font-bold mb-10 text-center">
          Генератор Moodle GIFT
        </h1>


        <div className="grid grid-cols-1 md:grid-cols-2 gap-10">

          <div>

            <label className="block mb-2 font-semibold text-lg">
              Нейросеть
            </label>

            <select
              value={provider}
              onChange={(e) => setProvider(e.target.value)}
              className="w-full border border-gray-300 rounded-xl p-4 mb-6 text-lg"
            >

              <option value="gigachat">
                GigaChat
              </option>

              <option value="chatgpt">
                ChatGPT
              </option>

            </select>


            <label className="block mb-2 font-semibold text-lg">
              Язык генерации
            </label>

            <select
              value={language}
              onChange={(e) => setLanguage(e.target.value)}
              className="w-full border border-gray-300 rounded-xl p-4 mb-6 text-lg"
            >

              <option value="ru">
                Русский
              </option>

              <option value="en">
                English
              </option>

            </select>


            <label className="block mb-2 font-semibold text-lg">
              Тематика вопросов
            </label>

            <input
              type="text"
              placeholder="Основы Python"
              value={topic}
              onChange={(e) => setTopic(e.target.value)}
              className="w-full border border-gray-300 rounded-xl p-4 mb-6 text-lg"
            />


            <label className="block mb-2 font-semibold text-lg">
              Тип вопроса
            </label>

            <select
              value={questionType}
              onChange={(e) => setQuestionType(e.target.value)}
              className="w-full border border-gray-300 rounded-xl p-4 mb-6 text-lg"
            >

              <option value="single">
                Один правильный ответ
              </option>

              <option value="boolean">
                Верно / Неверно
              </option>

              <option value="multiple">
                Множественный выбор
              </option>

            </select>


            <label className="block mb-2 font-semibold text-lg">
              Количество вопросов
            </label>

            <input
              type="number"
              value={questionsCount}
              onChange={(e) => setQuestionsCount(Number(e.target.value))}
              className="w-full border border-gray-300 rounded-xl p-4 mb-6 text-lg"
            />


            <label className="block mb-2 font-semibold text-lg">
              Количество вариантов ответа
            </label>

            <input
              type="number"
              value={answersCount}
              onChange={(e) => setAnswersCount(Number(e.target.value))}
              className="w-full border border-gray-300 rounded-xl p-4 mb-6 text-lg"
            />


            <label className="block mb-2 font-semibold text-lg">
              Текст для генерации вопросов
            </label>

            <textarea
              value={sourceText}
              onChange={(e) => setSourceText(e.target.value)}
              placeholder="Вставьте текст..."
              className="w-full h-[250px] border border-gray-300 rounded-xl p-4 mb-6 text-lg"
            />


            <button
              onClick={generateQuestions}
              disabled={loading}
              className="w-full bg-blue-600 text-white p-4 rounded-xl hover:bg-blue-700 transition text-lg font-semibold"
            >
              {
                loading
                  ? 'Генерация...'
                  : 'Сгенерировать вопросы'
              }
            </button>

          </div>


          <div>

            <div className="flex justify-between items-center mb-4">

              <h2 className="text-3xl font-semibold">
                Сгенерированные вопросы
              </h2>

              <div className="flex gap-3">

                {
                  giftResult && (
                    <button
                      onClick={copyGift}
                      className="bg-gray-700 text-white px-4 py-2 rounded-lg hover:bg-gray-800"
                    >
                      Копировать
                    </button>
                  )
                }

                {
                  giftResult && (
                    <button
                      onClick={downloadGift}
                      className="bg-green-600 text-white px-4 py-2 rounded-lg hover:bg-green-700"
                    >
                      Скачать .gift
                    </button>
                  )
                }

              </div>

            </div>


            <textarea
              value={giftResult}
              onChange={(e) => setGiftResult(e.target.value)}
              className="w-full h-[900px] border border-gray-300 rounded-xl p-4 font-mono text-sm bg-gray-50"
            />

          </div>

        </div>

      </div>

    </div>
  )
}

export default App