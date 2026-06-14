import { motion } from 'framer-motion'
import { Sparkles } from 'lucide-react'

interface GeneratorFormProps {

  language: string
  setLanguage: (value: string) => void

  modelProvider: string
  setModelProvider: (value: string) => void

  topic: string
  setTopic: (value: string) => void

  questionType: string
  setQuestionType: (value: string) => void

  questionsCount: number
  setQuestionsCount: (value: number) => void

  answersCount: number
  setAnswersCount: (value: number) => void

  sourceText: string
  setSourceText: (value: string) => void

  loading: boolean

  generateQuestions: () => void
}

export default function GeneratorForm({

  language,
  setLanguage,

  modelProvider,
  setModelProvider,

  topic,
  setTopic,

  questionType,
  setQuestionType,

  questionsCount,
  setQuestionsCount,

  answersCount,
  setAnswersCount,

  sourceText,
  setSourceText,

  loading,

  generateQuestions

}: GeneratorFormProps) {

  return (

    <motion.div
      whileHover={{ scale: 1.01 }}
      className="backdrop-blur-xl bg-white/10 border border-white/10 rounded-3xl p-8 shadow-2xl"
    >

      <div className="flex items-center gap-3 mb-6">

        <Sparkles className="text-blue-400" />

        <h2 className="text-2xl font-semibold">
          Параметры генерации
        </h2>

      </div>

      <div className="space-y-6">

        <div>

          <label className="block mb-2 text-slate-300">
            Язык генерации
          </label>

          <select
            value={language}
            onChange={(e) => setLanguage(e.target.value)}
            className="w-full bg-slate-900 border border-slate-700 rounded-xl p-4"
          >

            <option value="ru">
              Русский
            </option>

            <option value="en">
              English
            </option>

          </select>

        </div>

        <div>

          <label className="block mb-2 text-slate-300">
            Нейросеть
          </label>

          <select
            value={modelProvider}
            onChange={(e) =>
              setModelProvider(e.target.value)
            }
            className="w-full bg-slate-900 border border-slate-700 rounded-xl p-4"
          >

            <option value="gigachat">
              GigaChat
            </option>

          </select>

        </div>

        <div>

          <label className="block mb-2 text-slate-300">
            Тематика вопросов
          </label>

          <input
            type="text"
            placeholder="Основы Python"
            value={topic}
            onChange={(e) => setTopic(e.target.value)}
            className="w-full bg-slate-900 border border-slate-700 rounded-xl p-4"
          />

        </div>

        <div>

          <label className="block mb-2 text-slate-300">
            Тип вопроса
          </label>

          <select
            value={questionType}
            onChange={(e) => setQuestionType(e.target.value)}
            className="w-full bg-slate-900 border border-slate-700 rounded-xl p-4"
          >

            <option value="single">
              Один правильный ответ
            </option>

            <option value="truefalse">
              Верно / Неверно
            </option>

            <option value="multiple">
              Множественный выбор
            </option>

          </select>

        </div>

        <div className="grid grid-cols-2 gap-4">

          <div>

            <label className="block mb-2 text-slate-300">
              Кол-во вопросов
            </label>

            <input
              type="number"
              value={questionsCount}
              onChange={(e) =>
                setQuestionsCount(
                  Number(e.target.value)
                )
              }
              className="w-full bg-slate-900 border border-slate-700 rounded-xl p-4"
            />

          </div>

          <div>

            <label className="block mb-2 text-slate-300">
              Варианты ответа
            </label>

            <input
              type="number"
              value={answersCount}
              onChange={(e) =>
                setAnswersCount(
                  Number(e.target.value)
                )
              }
              className="w-full bg-slate-900 border border-slate-700 rounded-xl p-4"
            />

          </div>

        </div>

        <div>

          <label className="block mb-2 text-slate-300">
            Текст для генерации
          </label>

          <textarea
            value={sourceText}
            onChange={(e) =>
              setSourceText(e.target.value)
            }
            placeholder="Вставьте учебный материал..."
            className="w-full h-64 bg-slate-900 border border-slate-700 rounded-xl p-4"
          />

        </div>

        <motion.button
          whileHover={{ scale: 1.03 }}
          whileTap={{ scale: 0.97 }}
          onClick={generateQuestions}
          disabled={loading}
          className="w-full bg-gradient-to-r from-blue-500 to-purple-600 p-4 rounded-xl text-lg font-semibold shadow-lg"
        >

          {
            loading
              ? 'Генерация...'
              : 'Сгенерировать вопросы'
          }

        </motion.button>

      </div>

    </motion.div>
  )
}
