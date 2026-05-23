import { Brain } from 'lucide-react'

export default function Header() {

  return (

    <div className="flex items-center gap-4 mb-10">

      <div className="bg-blue-500 p-4 rounded-2xl shadow-lg">

        <Brain size={40} />

      </div>

      <div>

        <h1 className="text-5xl font-bold">
          Moodle GIFT Generator
        </h1>

        <p className="text-slate-300 mt-2 text-lg">
          AI генерация тестов для Moodle
        </p>

      </div>

    </div>
  )
}