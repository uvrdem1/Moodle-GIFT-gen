import { useState } from 'react'
import axios from 'axios'

import { motion } from 'framer-motion'

import Header from './components/Header'
import GeneratorForm from './components/GeneratorForm'
import QuestionsPreview from './components/QuestionsPreview'


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

      setGiftResult(
        response.data.gift
      )

    } catch (error) {

      console.error(error)

      alert(
        'Ошибка генерации'
      )

    } finally {

      setLoading(false)
    }
  }


  const downloadGift = () => {

    const blob = new Blob(
      [giftResult],
      {
        type: 'text/plain'
      }
    )

    const url = window.URL.createObjectURL(
      blob
    )

    const link = document.createElement('a')

    link.href = url

    link.download = 'questions.gift'

    link.click()

    window.URL.revokeObjectURL(url)
  }


  const copyGift = async () => {

    await navigator.clipboard.writeText(
      giftResult
    )

    alert('GIFT скопирован')
  }


  return (

    <div className="min-h-screen bg-gradient-to-br from-slate-950 via-blue-950 to-slate-900 text-white overflow-hidden">

      <div className="absolute top-0 left-0 w-96 h-96 bg-blue-500 opacity-20 blur-3xl rounded-full"></div>

      <div className="absolute bottom-0 right-0 w-96 h-96 bg-purple-500 opacity-20 blur-3xl rounded-full"></div>


      <div className="relative z-10 p-10">

        <motion.div
          initial={{
            opacity: 0,
            y: 40
          }}
          animate={{
            opacity: 1,
            y: 0
          }}
          transition={{
            duration: 0.7
          }}
          className="max-w-7xl mx-auto"
        >

          <Header />

          <div className="grid grid-cols-1 lg:grid-cols-2 gap-10">

            <GeneratorForm

              provider={provider}
              setProvider={setProvider}

              language={language}
              setLanguage={setLanguage}

              topic={topic}
              setTopic={setTopic}

              questionType={questionType}
              setQuestionType={setQuestionType}

              questionsCount={questionsCount}
              setQuestionsCount={setQuestionsCount}

              answersCount={answersCount}
              setAnswersCount={setAnswersCount}

              sourceText={sourceText}
              setSourceText={setSourceText}

              loading={loading}

              generateQuestions={generateQuestions}
            />


            <QuestionsPreview

              giftResult={giftResult}

              setGiftResult={setGiftResult}

              copyGift={copyGift}

              downloadGift={downloadGift}
            />

          </div>

        </motion.div>

      </div>

    </div>
  )
}

export default App